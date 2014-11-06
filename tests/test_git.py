from __future__ import print_function
import os
import subprocess

def test_fail(tmpdir):
    root_dir = os.getcwd()
    os.chdir(str(tmpdir))
    for path in ['helpers', 'calculate_stats.py', 'statsrunner', 'stats']:
        os.symlink(os.path.join(root_dir, path), os.path.join(str(tmpdir), path))
    subprocess.call('''
        mkdir -p data/test_publisher
        cd data
        git init
        touch test_publisher/empty.xml;
        git add .
        git commit -a -m "Commit 1"
        cd ..
        ''', shell=True)
    subprocess.call(os.path.join(root_dir, 'git.sh'))

    gitout_files = os.listdir(os.path.join(str(tmpdir), 'gitout'))
    for expected_file in [
            'commits',
            'current',
            'current.tar.gz',
            'gitaggregate',
            'gitaggregate-dated',
            'gitaggregate.tar.gz',
            'gitaggregate-dated.tar.gz',
            'gitaggregate-publisher',
            'gitaggregate-publisher-dated',
            'gitaggregate-publisher.tar.gz',
            'gitaggregate-publisher-dated.tar.gz',
            'gitdate.json',
            'ckan.json',
            ]:
        assert expected_file in gitout_files

    gitout_current_files = os.listdir(os.path.join(str(tmpdir), 'gitout', 'current'))
    for expected_file in [
            'aggregated',
            'aggregated-file',
            'aggregated-publisher',
            'inverted-file',
            'inverted-file-publisher',
            'inverted-publisher',
            ]:
        assert expected_file in gitout_current_files