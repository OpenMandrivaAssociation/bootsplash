%define debug_package %{nil}

Summary:	Scripts to handle Mandriva themeing
Name:		bootsplash
Version:	3.4.1
Release:	9
# From Mandriva SVN
Source0:	%{name}-%{version}.tar.xz
License:	GPL
Group:		System/Kernel and hardware
Url:		http://abf.rosalinux.ru/omv_software/bootsplash/
Patch0:		bootsplash-3.4.0-fix-xz-compression-settings.patch
Requires:	perl-base
# Do not require mkinitrd anymore to be able to be prerequed by mkinitrd (mkinitrd is in basesystem anyway)
# Requires: mkinitrd >= 3.5.18-14mdk
Conflicts:	mkinitrd < 3.5.18-14mdk
#there is no way to say a special kernel requires.
%ifnarch %arm aarch64
Requires:	kernel
%endif
Requires:	initscripts > 7.04-15mdk
Requires:	perl-Archive-Cpio
Suggests:	drakx-kbd-mouse-x11 >= 0.102-4
%ifnarch %arm aarch64
Requires:	plymouth-scripts
%endif
Conflicts:	drakxtools-newt < 10-49mdk

%description
This package contains the scripts necessary to install and change the theme 
used by Mandriva (at boot time and in desktop sessions).

%prep
%setup -q
%apply_patches

%build
make LIB=%{_lib}

%install
make install prefix=%{buildroot}

%files
%doc README ChangeLog
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/scripts
