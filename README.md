# DLL Export List

Collection of dll export function list, in tsv format

## Usage

1. Install python3 and lief
2. `python3 gen_db.py /mnt/c/Windows/System32/*.[Dd][Ll][Ll]` (I'm using WSL)

## TODO

- [ ] Load db file and de-duplicate output
- [ ] Add common hash function used by shellcode/malware and lookup tool
- [ ] Fancy commandline interface

## Other Awesome Resources

Check shellcode\_hashes from
[fireeye/flare-ida](https://github.com/fireeye/flare-ida/tree/master/shellcode_hashes) and the
[IDA Pro plugin](https://github.com/fireeye/flare-ida/blob/master/plugins/shellcode_hashes_search_plugin.py),
it's awesome!

## Notes

Current db was generated from Windows 10 x64 1909 (OS Build 18363.1139),
and lief version: `0.9.0-a448c5e`

## LICENSE

CC0
