#!/usr/bin/env python3
#
# Purpose: TODO
#
# Recursively crawl flexelint_outdir and read all "*.out" files
# Then compute how many lines contain "Error", "Warning", "Info", "Note"
# and collect statistics broken out by MISRA Rule#
# When finished, dump the result to a JSON structure

import os
import re

# print("Hello, world!")

# FIXME: Should parse command line parameters instead
flexelint_outdir = "/home/gmacario/tmp/linux-4.4.50-min-lint"
linux_sourcedir = "/home/gmacario/minimized-tree-v4.4.50-bradocaj"


# Data structure to collect statistics for each MISRA Rule

"""
stats_misra_rules = [
    {'id': '3.1', 'n_line': 198, 'n_error': 10, 'n_warning': 30, 'n_info': 100, 'n_note': 50},
]
"""

stats_misra_rules = {}

def dump_rulestats(s):
    print('DEBUG; dump_rulestats(s=%s)' % s)
    for key in s:
        print('DEBUG: dump_rulestats: key %s ==> val %s' % (key, s[key]))
    return None

def inc_rulestats(s, rulenum, is_error, is_warning, is_info, is_note):
    print('DEBUG: inc_rulestats: s=%s' % s)
    oldval = s.get(rulenum, {
        'rulenum': rulenum,
        'n_line': 0,
        'n_error': 0,
        'n_warning': 0,
        'n_info': 0,
        'n_note': 0
    })
    print('DEBUG: inc_rulestats: oldval=%s' % oldval)
    newval = {
        'rulenum':   rulenum,
        'n_line':    oldval['n_line'] + 1,
        'n_error':   oldval['n_error'] + is_error,
        'n_warning': oldval['n_warning'] + is_warning,
        'n_info':    oldval['n_info'] + is_info,
        'n_note':    oldval['n_note'] + is_note
    }
    print('DEBUG: inc_rulestats: newval=%s' % newval)
    s[rulenum] = newval
    # dump_rulestats(s)
    return None

def handle_line(line):
    print('DEBUG: handle_line: line=%s' % line)
    is_error   = (re.search(r' Error \d+\:',   line) != None)
    is_warning = (re.search(r' Warning \d+\:', line) != None)
    is_info    = (re.search(r' Info \d+\:',    line) != None)
    is_note    = (re.search(r' Note \d+\:',    line) != None)
    # Handle case of multiple MISRA violations for the same line
    pos = 0;
    while pos < len(line):
        searchObj = re.search(r'\[MISRA 2012 Rule (\d+\.\d+)[^\]]*\]', line[pos:], re.M)
        # print('DEBUG: handle_line: searchObj=%s' % searchObj)
        if searchObj == None:
            break;
        misra_rulenum = searchObj.group(1)
        print('TODO: Update stats_misra_rules: rulenum=%s, is_error=%d, is_warning=%d, is_info=%d, is_note=%d' % (misra_rulenum, is_error, is_warning, is_info, is_note))
        inc_rulestats(stats_misra_rules, misra_rulenum, is_error, is_warning, is_info, is_note)
        pos = pos + searchObj.end()
        # print('DEBUG: misra_rulenum=%s, new_pos=%d' % (misra_rulenum, pos))
    return None

def compute_statistics(report_path, module_name):
    # print('DEBUG: compute_statistics(report_path=%s, module_name=%s)' % (report_path, module_name))
    with open(report_path, errors='replace') as f:
        # print('DEBUG: compute_statistics: f=%s' % f)
        i = 0;
        for line in f:
            i = i + 1
            for i, line in enumerate(f):
                # print('DEBUG: i=%d, line=%s' % (i, line))
                if line.find('MISRA 2012') != -1:
                    handle_line(line)
    # TODO
    return None

def traverse_tree(rootdir):
    """Traverse a Directory Tree
    See also:
    * https://docs.python.org/3/library/os.html
    * https://www.pythoncentral.io/how-to-traverse-a-directory-tree-in-python-guide-to-os-walk/
    """
    print('DEBUG: traverse_tree(rootdir=%s)' % rootdir)
    for dirpath, dirnames, filenames in os.walk(rootdir):
        # print('DEBUG: Found directory: %s' % dirpath)
        for fname in filenames:
            # print('DEBUG: Found file: \t%s' % fname)
            if fname.endswith('.out'):
                report_path = dirpath + '/' + fname
                module_name = '.' + dirpath[len(rootdir):] + '/' + fname[0:len(fname)-4]
                # print('TODO: compute_statistics(%s, %s)' % (report_path, module_name))
                compute_statistics(report_path, module_name)

def main():
    # traverse_tree('.')
    traverse_tree(flexelint_outdir)

# ---------------------------------

if __name__ == '__main__':
    main()

# EOF
