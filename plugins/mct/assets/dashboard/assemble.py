#!/usr/bin/env python3
"""Assemble dashboard: read project data, inject into template, write output."""
import json
import os
import sys
from datetime import datetime


def read_json(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def scan_dir(dirpath, rel_base='.'):
    """Scan directory for files. Read MD content; list others as binary.
    Paths are made relative to rel_base (the dashboard output directory)."""
    files = []
    if not os.path.isdir(dirpath):
        return files
    for fname in sorted(os.listdir(dirpath)):
        fpath = os.path.join(dirpath, fname)
        if not os.path.isfile(fpath):
            continue
        entry = {'filename': fname, 'path': os.path.relpath(fpath, rel_base)}
        if fname.endswith('.md'):
            try:
                with open(fpath, 'r', encoding='utf-8') as f:
                    entry['content'] = f.read()
                entry['type'] = 'md'
            except Exception:
                entry['content'] = None
                entry['type'] = 'error'
        else:
            entry['content'] = None
            ext = os.path.splitext(fname)[1].lower()
            entry['type'] = ext.lstrip('.') if ext else 'unknown'
        files.append(entry)
    return files


def scan_client_data(dirpath):
    """Scan client-data/ and client-data/inbox/ for uploaded files."""
    files = []
    if not os.path.isdir(dirpath):
        return files
    for root, _, fnames in os.walk(dirpath):
        for fname in sorted(fnames):
            fpath = os.path.join(root, fname)
            ext = os.path.splitext(fname)[1].lower().lstrip('.')
            files.append({
                'filename': fname,
                'path': os.path.relpath(fpath, dirpath),
                'type': ext or 'unknown'
            })
    return files


def scan_agent_memory(dirpath):
    """Scan agent-memory/ for each agent's memory.md, feedback.md, and tasks.md."""
    agents = {}
    if not os.path.isdir(dirpath):
        return agents
    for name in sorted(os.listdir(dirpath)):
        agent_dir = os.path.join(dirpath, name)
        if not os.path.isdir(agent_dir):
            continue
        agent = {'name': name}
        for fname in ['memory.md', 'feedback.md', 'tasks.md']:
            fpath = os.path.join(agent_dir, fname)
            if os.path.isfile(fpath):
                try:
                    with open(fpath, 'r', encoding='utf-8') as f:
                        agent[fname.replace('.md', '')] = f.read()
                except Exception:
                    pass
        agents[name] = agent
    return agents


def main():
    if len(sys.argv) < 4:
        print("Usage: assemble.py <project-data-dir> <template-path> <output-path>",
              file=sys.stderr)
        sys.exit(1)

    pd = sys.argv[1]
    template_path = sys.argv[2]
    output_path = sys.argv[3]
    out_dir = os.path.dirname(os.path.abspath(output_path))

    data = {
        'engagement':    read_json(os.path.join(pd, 'engagement.json')),
        'hypotheses':    read_json(os.path.join(pd, 'hypotheses.json')),
        'workstreams':   read_json(os.path.join(pd, 'workstreams.json')),
        'drumbeat':      read_json(os.path.join(pd, 'drumbeat.json')),
        'tasks':         read_json(os.path.join(pd, 'tasks.json')),
        'document_registry': read_json(os.path.join(pd, 'document-registry.json')),
        'sources':       read_json(os.path.join(pd, 'sources', 'source-registry.json')),
        'deliverables':  scan_dir(os.path.join(pd, 'deliverables'), pd),
        'research':      scan_dir(os.path.join(pd, 'research'), pd),
        'analysis':      scan_dir(os.path.join(pd, 'analysis'), pd),
        'models':        scan_dir(os.path.join(pd, 'models'), pd),
        'findings':      scan_dir(os.path.join(pd, 'findings'), pd),
        'reviews':       scan_dir(os.path.join(pd, 'reviews'), pd),
        'client_data':   scan_client_data(os.path.join(pd, 'client-data')),
        'agent_memory':  scan_agent_memory(os.path.join(pd, 'agent-memory')),
        'build_time':    datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    }

    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    injected = json.dumps(data, ensure_ascii=False, indent=None)
    output = template.replace('__INJECT_DATA__', injected)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f"Dashboard written to {output_path}")


if __name__ == '__main__':
    main()
