#!/bin/bash
# IOC scanner for triage lab
grep -r -i "185.130.5.253" data/logs/
grep -r -i "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855" data/logs/