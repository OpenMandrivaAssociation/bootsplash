%define name bootsplash
%define version 3.3.1
%define release %mkrel 1

Summary: Scripts to handle Mandriva themeing
Name: %{name}
Version: %{version}
Release: %{release}
# From Mandriva SVN
Source0: %{name}-%version.tar.bz2
License: GPL
Group: System/Kernel and hardware
BuildRoot: %{_tmppath}/%{name}-buildroot
Url:       http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/bootsplash/
Requires: perl-base
# Do not require mkinitrd anymore to be able to be prerequed by mkinitrd (mkinitrd is in basesystem anyway)
# Requires: mkinitrd >= 3.5.18-14mdk
Conflicts: mkinitrd < 3.5.18-14mdk
#there is no way to say a special kernel requires.
Requires: kernel initscripts > 7.04-15mdk 
Requires: perl-Archive-Cpio
Suggests: drakx-kbd-mouse-x11
Requires: plymouth-scripts
Conflicts: drakxtools-newt < 10-49mdk
BuildArchitectures: noarch

%description
This package contains the scripts necessary to install and change the theme 
used by Mandriva (at boot time and in desktop sessions)

%prep
%setup -q

%build
make LIB=%{_lib}

%install
rm -rf %{buildroot}
make install prefix=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README ChangeLog 
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/scripts


