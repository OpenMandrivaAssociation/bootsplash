%define debug_package %{nil}

Summary:	Scripts to handle Mandriva themeing
Name:		bootsplash
Version:	3.4.2
Release:	9
# From Mandriva SVN
Source0:	%{name}-%{version}.tar.xz
License:	GPL
Group:		System/Kernel and hardware
Url:		https://abf.rosalinux.ru/omv_software/bootsplash/
# Do not require mkinitrd anymore to be able to be prerequed by mkinitrd (mkinitrd is in basesystem anyway)
# Requires: mkinitrd >= 3.5.18-14mdk
Conflicts:	mkinitrd < 3.5.18-14mdk
#there is no way to say a special kernel requires.
%ifnarch %arm aarch64
Requires:	kernel
%endif
Requires:	initscripts > 7.04-15mdk
%ifnarch %arm
Requires:	plymouth-scripts
%endif
Conflicts:	drakxtools-newt < 10-49mdk

%description
This package contains the scripts necessary to install and change the theme 
used by Mandriva (at boot time and in desktop sessions).

%prep
%setup -q
%autopatch -p1

%build
make LIB=%{_lib}

%install
make install prefix=%{buildroot}

%files
%doc README ChangeLog
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/scripts
