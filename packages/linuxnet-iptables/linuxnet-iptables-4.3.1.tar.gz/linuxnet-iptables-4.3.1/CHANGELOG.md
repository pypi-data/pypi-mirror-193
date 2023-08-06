Change Log
==========

4.3.1 (2023-02-20)
------------------

- Added method to Chain/IptablesPacketFilterTable class to zero the packet/byte
  counters of a specific chain, or all chains

4.2.1 (2023-02-07)
------------------

- Fixed bug in LogTarget class

4.2.0 (2023-02-06)
------------------

- added framework for extending the linuxnet.iptables package
  with new xxxMatch and xxxTarget classes to support additional
  iptables match and target extensions
- added new section in the documentation with information
  on how to add new match/target classes (including examples)
- reworked package module structure:
    * monolithic match.py module broken into per-match-class modules
    * monolithic target.py module broken into per-target-class modules
- all CONNMARK target options are now supported
- added support for 'owner' match
- added mask support in MarkMatch and ConnmarkMatch classes
- the IcmpTypeCriterion now supports the complete list of ICMP types
  and ICMP codes
- The following changes were backwards-incompatible, and resulted
  in the bumpting of the major version number:
    * the xxxCriterion classes are no longer in the linuxnet.iptables
      namespace
    * the Criterion.equals() method is no longer implemented
    * the MssCriterion value changed from a string to a tuple of integers
    * the RateLimitCriterion value changed from integer to a
      LimitMatch.Rate object
    * the RateLimitCriterion rate2spec and spec2rate methods were removed
    * replaced the LogTarget.set_log_options() method with
      option-specific methods

3.2.0 (2023-01-27)
------------------

- Improved MARK/CONNMARK target support
- Reworked documentation

3.1.0 (2023-01-21)
------------------

- Added support for the TTL target
- Added support for the TTL match

3.0.1 (2022-12-31)
------------------

- First published release

