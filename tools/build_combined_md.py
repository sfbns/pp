"""Merge the latest deliverables into one Markdown file with renderer-safe formatting.

Usage: python3 -I tools/build_combined_md.py <cover.md> <out.md> <deliverable1.md> [<deliverable2.md> ...]

What it does (the source files are not modified):
  * strips each file's YAML front matter and turns title/subtitle/date into a level-1 heading plus a quote line;
  * demotes all headings by one level (outside fenced code blocks);
  * makes every '---' rule safe (blank line before it, so it never becomes a setext heading);
  * inside math: '*' -> '\\ast', '<' followed by a letter -> '< ' (avoids HTML-tag parsing), circled digits -> (1)(2)...,
    '|' inside inline math on table rows -> '\\vert' (avoids splitting table cells);
  * guarantees blank lines around display-math blocks.
"""
import re
import sys

FENCE = re.compile(r'^\s*(```|~~~)')


def split_front_matter(text):
    meta, body = {}, text
    if text.startswith('---\n'):
        end = text.find('\n---\n', 4)
        if end != -1:
            for line in text[4:end].splitlines():
                m = re.match(r'^(\w+):\s*"?(.*?)"?\s*$', line)
                if m:
                    meta[m.group(1)] = m.group(2)
            body = text[end + 5:]
    return meta, body


def fix_math(tex, in_table_row=False):
    tex = tex.replace('^{***}', r'^{\ast\ast\ast}').replace('^{**}', r'^{\ast\ast}').replace('^{*}', r'^{\ast}')
    tex = re.sub(r'\^\*', r'^{\\ast}', tex)
    tex = tex.replace('*', r'\ast ')
    tex = re.sub(r'<(?=[A-Za-z/!?])', '< ', tex)
    for k, v in zip('①②③④⑤⑥⑦⑧⑨', ['(1)', '(2)', '(3)', '(4)', '(5)', '(6)', '(7)', '(8)', '(9)']):
        tex = tex.replace(k, v)  # circled digits lack KaTeX font metrics
    if in_table_row:
        tex = re.sub(r'(?<!\\)\|', r'\\vert ', tex)
    return tex


INLINE = re.compile(r'(?<!\\)\$(?!\$)(.+?)(?<!\\)\$')


def fix_inline_line(line):
    in_table = line.lstrip().startswith('|')
    # protect inline code spans
    parts = re.split(r'(`[^`]*`)', line)
    out = []
    for part in parts:
        if part.startswith('`') and part.endswith('`') and len(part) > 1:
            out.append(part)
        else:
            out.append(INLINE.sub(lambda m: '$' + fix_math(m.group(1), in_table) + '$', part))
    return ''.join(out)


def transform_body(body):
    lines = body.splitlines()
    out = []
    in_code = False
    in_display = False
    display_buf = []
    for line in lines:
        if in_code:
            out.append(line)
            if FENCE.match(line):
                in_code = False
            continue
        if in_display:
            if line.strip() == '$$':
                out.append(fix_math('\n'.join(display_buf)))
                out.append('$$')
                out.append('')
                in_display = False
                display_buf = []
            else:
                display_buf.append(line)
            continue
        if FENCE.match(line):
            in_code = True
            out.append(line)
            continue
        stripped = line.strip()
        if stripped == '$$':
            if out and out[-1].strip() != '':
                out.append('')
            out.append('$$')
            in_display = True
            continue
        if re.match(r'^\$\$.*\$\$\s*$', stripped) and len(stripped) > 4:
            if out and out[-1].strip() != '':
                out.append('')
            out.append('$$' + fix_math(stripped[2:-2]) + '$$')
            out.append('')
            continue
        if re.match(r'^#{1,5}\s', line):
            line = '#' + line
        elif stripped == '---':
            if out and out[-1].strip() != '':
                out.append('')
            out.append('---')
            continue
        out.append(fix_inline_line(line))
    if in_display or in_code:
        raise SystemExit('unterminated display math or code block')
    text = '\n'.join(out)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip('\n')


def section_from_file(path, is_cover=False):
    text = open(path, encoding='utf-8').read()
    meta, body = split_front_matter(text)
    title = meta.get('title', path)
    sub = meta.get('subtitle', '')
    date = meta.get('date', '')
    head = ['# ' + title, '']
    info = '；'.join(x for x in (sub, date) if x)
    if info:
        head += ['> ' + info, '']
    return '\n'.join(head).rstrip('\n') + '\n\n' + transform_body(body), title


def main():
    cover, out_path, files = sys.argv[1], sys.argv[2], sys.argv[3:]
    cover_text, cover_title = section_from_file(cover, is_cover=True)
    sections, titles = [], []
    for f in files:
        sec, t = section_from_file(f)
        sections.append(sec)
        titles.append(t)
    toc = ['## 目录（各部分）', '']
    for i, t in enumerate(titles, 1):
        toc.append(f'{i}. {t}')
    doc = cover_text + '\n\n' + '\n'.join(toc) + '\n\n---\n\n' + '\n\n---\n\n'.join(sections) + '\n'
    open(out_path, 'w', encoding='utf-8').write(doc)
    print(f'wrote {out_path}: {len(doc.splitlines())} lines, {len(files)} parts')


if __name__ == '__main__':
    main()
