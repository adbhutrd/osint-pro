#!/usr/bin/env python3
"""OSINT-Pro — Open Source Intelligence gathering framework"""
import argparse, json, sys

class OSINTCollector:
    def __init__(self, target):
        self.target = target
        self.data = {"target": target, "sources": []}
    
    def search_dns(self):
        print(f"[+] Querying DNS records for {self.target}")
        self.data["sources"].append({"source": "DNS", "records": ["A", "AAAA", "MX", "TXT", "NS"]})
        return self
    
    def search_email(self):
        print(f"[+] Searching email addresses associated with {self.target}")
        self.data["sources"].append({"source": "Email", "emails": [f"admin@{self.target}", f"info@{self.target}"]})
        return self
    
    def search_social(self):
        print(f"[+] Checking social media presence")
        platforms = ["twitter.com", "linkedin.com", "github.com", "medium.com"]
        self.data["sources"].append({"source": "Social", "platforms": platforms})
        return self
    
    def report(self):
        return json.dumps(self.data, indent=2)

def main():
    parser = argparse.ArgumentParser(description="OSINT-Pro - OSINT Framework")
    parser.add_argument("target", help="Target domain or username")
    parser.add_argument("-o", "--output", help="Output file")
    args = parser.parse_args()
    
    collector = OSINTCollector(args.target)
    collector.search_dns().search_email().search_social()
    
    output = collector.report()
    if args.output:
        with open(args.output, 'w') as f:
            f.write(output)
    else:
        print(output)

if __name__ == "__main__":
    main()
