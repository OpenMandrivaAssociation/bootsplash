%define name bootsplash
%define version 3.2.16
%define release %mkrel 1

Summary: The Boot Splash Images and scripts
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
Requires: kernel initscripts > 7.04-15mdk fbgrab
Requires: perl-Archive-Cpio
Conflicts: drakxtools-newt < 10-49mdk
Obsoletes: Aurora Aurora-Monitor-NewStyle-Categorizing-WsLib Aurora-Monitor-NewStyle-WsLib Aurora-Monitor-Traditional-Gtk+ Aurora-Monitor-Traditional-WsLib-8.2
BuildRequires: freetype2-static-devel libmng-static-devel libjpeg-static-devel glibc-static-devel lcms-devel gtk-linux-fb-2.0-devel gtk+2-devel
# nomore noarch with the fbrelolution and progress binaries
#BuildArchitectures: noarch

%description
This package contains the scripts and pictures visible when booting a
Mandriva Linux kernel.  They are automatically installed when an initrd is
generated by mkinitrd.

%prep
%setup -q

%build
make LIB=%{_lib}

%install
rm -rf %{buildroot}
make install prefix=%{buildroot}

install -m 755 -d %{buildroot}%{_sysconfdir}/%{name}

for i in fbmngplay fbtruetype 
do
   cp $i/ChangeLog $i/ChangeLog.$i
   cp $i/README $i/README.$i
done

#find %{buildroot}/%{_sysconfdir}/%{name}/ %{buildroot}/%_datadir/%{name}/ -not -path "*/themes/Mandrake/*" -not -path "*/scripts/*" -type f |
#  sed -e "s#^%{buildroot}##g" > rpm-themes-files

install -d -m755 %{buildroot}%{_sysconfdir}/%{name}/themes
install -d -m755 %{buildroot}%{_datadir}/%{name}/themes

%find_lang bootsplash

%post
# Add right translation file
for i in `echo $LANGUAGE:$LC_ALL:$LC_COLLATE:$LANG:C | tr ':' ' '`
do      
        if [ -r %{_datadir}/locale/$i/LC_MESSAGES/bootsplash.mo ]; then
                mkdir -p /etc/locale/$i/LC_MESSAGES/
                cp %{_datadir}/locale/$i/LC_MESSAGES/SYS_LC_MESSAGES \
                        /etc/locale/$i/LC_MESSAGES/
                cp %{_datadir}/locale/$i/LC_MESSAGES/bootsplash.mo \
                        /etc/locale/$i/LC_MESSAGES/
            break
        fi
done
%if %mdkversion < 200900
/sbin/ldconfig
%endif
    
%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%doc README ChangeLog fbmngplay/ChangeLog.fbmngplay fbmngplay/README.fbmngplay fbtruetype/ChangeLog.fbtruetype fbtruetype/README.fbtruetype
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/themes
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/themes
%{_datadir}/%{name}/scripts
#%_datadir/%{name}/themes/Mandrake
#%config(noreplace) %_sysconfdir/%{name}/themes/Mandrake/*
/bin/fbresolution
/bin/fbtruetype.static
/bin/fbmngplay.static
/bin/progress
/sbin/bootanim
/sbin/splash
/sbin/splash.sh
%{_bindir}/*


