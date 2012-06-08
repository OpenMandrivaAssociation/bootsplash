Summary:	Scripts to handle Mandriva themeing
Name:		bootsplash
Version:	3.4.0
Release:	2
# Generate from a git checkout using
# git archive --format=tar --prefix=bootsplash-%version/ -o bootsplash-%version.tar master ; xz -9e bootsplash-%version.tar
Source0:	%{name}-%version.tar.xz
Patch0:		bootsplash-3.4.0-fix-xz-compression-settings.patch
License:	GPL
Group:		System/Kernel and hardware
Url:		http://git.mandriva.com/projects/?p=soft/bootsplash.git
Requires:	perl-base
# Do not require mkinitrd anymore to be able to be prerequed by mkinitrd (mkinitrd is in basesystem anyway)
# Requires: mkinitrd >= 3.5.18-14mdk
Conflicts:	mkinitrd < 3.5.18-14mdk
#there is no way to say a special kernel requires.
Requires:	kernel initscripts > 7.04-15mdk 
Requires:	perl-Archive-Cpio
Suggests:	drakx-kbd-mouse-x11
Requires:	plymouth-scripts
Conflicts:	drakxtools-newt < 10-49mdk
BuildArchitectures: noarch

%description
This package contains the scripts necessary to install and change the theme 
used by Mandriva (at boot time and in desktop sessions)

%prep
%setup -q
%patch0 -p1 -b .xz_crc32~

%build
make LIB=%{_lib}

%install
make install prefix=%{buildroot}

%files
%doc README ChangeLog 
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/scripts
