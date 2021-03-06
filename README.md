[![Latest release](https://img.shields.io/github/release/petrs/gpalist.svg)](https://github.com/petrs/gpalist/releases/latest) [![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/petrs/jcAIDScan/blob/master/LICENSE) 

# gpalist - an augmented output of GlobalPlatformPro tool 

A simple python scripts which execute marvelous [GlobalPlatformPro](https://github.com/martinpaljak/GlobalPlatformPro) tool by Martin Paljak, list applets available on target card (*'gp --list'*) and augment original output with names for well-known Applications Identifiers (AIDs) and Registered Application Provider Identifiers (RIDs). 

The well-known AIDs and RIDs are read from *well_known_aids.csv* and *well_known_rids.csv* originally compiled by [eftlab](https://www.eftlab.co.uk/) ([aid](https://www.eftlab.com.au/knowledge-base/211-emv-aid-rid-pix/), [rid](https://www.eftlab.com.au/knowledge-base/212-emv-rid)). Please create a pull request if you would like to add additional known applet AID or vendor.

## Setup
Already installed [GlobalPlatformPro tool](https://github.com/martinpaljak/GlobalPlatformPro) is assumed. The augmentation works both with older and newer output formatting.

Please edit constants GP_BASIC_COMMAND and GP_AUTH_FLAG in *run.py* if necessary. 
On Windows, set to 
```python
GP_BASIC_COMMAND = 'gp.exe'
```
while on Linux set to 
```python
GP_BASIC_COMMAND = 'run_gp.sh'
```
GP_AUTH_FLAG is usually left as an empty string. Only if GlobalPlatform SCP authentication protocol requires different key derivation algorithm (e.g., used for G&D cards), change to
```python
GP_AUTH_FLAG = '--emv'  
```

## Example
Original output after running 'gp --list':
```vim
>gp --list
AID: A000000003000000 (|........|)
     ISD OP_READY: Security Domain, Card lock, Card terminate, Default selected, CVM (PIN) management

AID: A000000527210101 (|....'!..|)
     App SELECTABLE: (none)

AID: D2760000986C6962 (|.v...lib|)
     ExM LOADED: (none)

AID: A0000001320001 (|....2..|)
     ExM LOADED: (none)

AID: D27600009861757468 (|.v...auth|)
     ExM LOADED: (none)

AID: A0000005272101 (|....'!.|)
     ExM LOADED: (none)
     A000000527210101 (|....'!..|)
```

Augmented output after running gp via 'run.py':
```vim
>run.py
AID: A000000003000000 (|........|)
     RID info: A000000003, Vendor: Visa International / United States
     AID info: (VISA) Card Manager, Used by most GP2.1.1 cards / Oberthur OP201 cards. Visa Proprietary Card Manager AID for OpenPlatform cards (visa.openplatform)., Vendor: Visa International / United States
     ISD OP_READY: Security Domain, Card lock, Card terminate, Default selected, CVM (PIN) management

AID: A000000527210101 (|....'!..|)
     RID info: A000000527, Vendor: Yubico / Sweden
     AID info: Yubikey NEO OATH Applet, Javacard Applet AID, Vendor: Yubico / Sweden
     App SELECTABLE: (none)

AID: D2760000986C6962 (|.v...lib|)
     RID info: D276000098, Vendor: Cryptovision / Germany
     AID info: unknown AID
     ExM LOADED: (none)

AID: A0000001320001 (|....2..|)
     RID info: A000000132, Vendor: Java Card Forum / United States
     AID info: org.javacardforum.javacard.biometry, , Vendor: Java Card Forum / United States
     ExM LOADED: (none)

AID: D27600009861757468 (|.v...auth|)
     RID info: D276000098, Vendor: Cryptovision / Germany
     AID info: unknown AID
     ExM LOADED: (none)

AID: A0000005272101 (|....'!.|)
     RID info: A000000527, Vendor: Yubico / Sweden
     AID info: unknown AID
     ExM LOADED: (none)
     A000000527210101 (|....'!..|)
```
