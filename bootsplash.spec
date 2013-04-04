Summary:	Scripts to handle Mandriva themeing
Name:		bootsplash
Version:	3.4.0
Release:	3
# From Mandriva SVN
Source0:	%{name}-%{version}.tar.bz2
License:	GPL
Group:		System/Kernel and hardware
Url:		http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/bootsplash/
Patch0:		bootsplash-3.4.0-fix-xz-compression-settings.patch
Requires:	perl-base
# Do not require mkinitrd anymore to be able to be prerequed by mkinitrd (mkinitrd is in basesystem anyway)
# Requires: mkinitrd >= 3.5.18-14mdk
Conflicts:	mkinitrd < 3.5.18-14mdk
#there is no way to say a special kernel requires.
Requires:	kernel
Requires:	initscripts > 7.04-15mdk
Requires:	perl-Archive-Cpio
Suggests:	drakx-kbd-mouse-x11
Requires:	plymouth-scripts
Conflicts:	drakxtools-newt < 10-49mdk
BuildArch:	noarch

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




%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 3.3.3-3mdv2011.0
+ Revision: 663333
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 3.3.3-2mdv2011.0
+ Revision: 603766
- rebuild

* Sun Nov 29 2009 Pascal Terjan <pterjan@mandriva.org> 3.3.3-1mdv2010.1
+ Revision: 471342
- Fix files exclusion (#56069)
- Compress with gzip -9 like done in oriiginal initrd

* Fri Nov 27 2009 Christophe Fergeau <cfergeau@mandriva.com> 3.3.2-1mdv2010.1
+ Revision: 470685
- 3.3.2:
- don't add duplicate files in initrd

* Mon Oct 12 2009 Frederic Crozat <fcrozat@mandriva.com> 3.3.1-1mdv2010.0
+ Revision: 456872
- Release 3.3.1 :
 - hide more error messages when processing invalid initrd
 - do not update backgrounds links for each initrd processing

* Wed Oct 07 2009 Frederic Crozat <fcrozat@mandriva.com> 3.3.0-1mdv2010.0
+ Revision: 455682
- Release 3.3.0 :
 - support for plymouth (and drop splashy support)

  + Christophe Fergeau <cfergeau@mandriva.com>
    - adjust .spec to bootsplash cleanup (removal of obsolete stuff)

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 3.2.25-2mdv2010.0
+ Revision: 413182
- rebuild

* Tue Apr 21 2009 Frederic Crozat <fcrozat@mandriva.com> 3.2.25-1mdv2009.1
+ Revision: 368553
- Release 3.2.25 :
 - prevent chvt deadlock in speedboot mode (Mdv bug #49946)
 - Fix text corrution in chinese on startup (tvignaud) (Mdv bug #35465)
 - Update translations

* Wed Apr 15 2009 Thierry Vignaud <tv@mandriva.org> 3.2.24-1mdv2009.1
+ Revision: 367386
- updated translations

* Mon Mar 30 2009 Frederic Crozat <fcrozat@mandriva.com> 3.2.23-1mdv2009.1
+ Revision: 362472
- Release 3.2.23 :
 - hide a lot of default splashy message by default
 - don't use splashy_update repaint to ping if splashy is alive
 - hide error message about /proc/cmdline not present at shutdown

* Fri Mar 27 2009 Frederic Crozat <fcrozat@mandriva.com> 3.2.22-1mdv2009.1
+ Revision: 361631
- Release 3.2.22 :
 - hide error message from splashy_config repaint call, since we use it to ping splashy

* Wed Mar 25 2009 Frederic Crozat <fcrozat@mandriva.com> 3.2.21-1mdv2009.1
+ Revision: 361003
- Release 3.2.21 :
 - ensure shutdown text is visible when using splashy

* Tue Mar 24 2009 Frederic Crozat <fcrozat@mandriva.com> 3.2.20-1mdv2009.1
+ Revision: 360867
- Release 3.2.20 :
 - fix font name for various languages

* Tue Feb 10 2009 Frederic Crozat <fcrozat@mandriva.com> 3.2.19-1mdv2009.1
+ Revision: 339155
- Release 3.2.19 :
- really fix changing splash theme

* Fri Feb 06 2009 Frederic Crozat <fcrozat@mandriva.com> 3.2.18-1mdv2009.1
+ Revision: 338225
- Release 3.2.18 :
 - fix location of splashy themes

* Wed Sep 24 2008 Olivier Blin <oblin@mandriva.com> 3.2.17-1mdv2009.0
+ Revision: 287661
- 3.2.17
- fix clearing tty8 and switching to tty1 when splashy has been stopped

* Wed Aug 27 2008 Olivier Blin <oblin@mandriva.com> 3.2.16-1mdv2009.0
+ Revision: 276575
- 3.2.16
- set DURING_MAKE_BOOTSPLASH variable when calling splashy_config

* Tue Aug 05 2008 Olivier Blin <oblin@mandriva.com> 3.2.15-1mdv2009.0
+ Revision: 263883
- 3.2.15
- do not warn about missing /proc/splash if in splashy mode (#42459)

* Tue Jul 29 2008 Olivier Blin <oblin@mandriva.com> 3.2.14-1mdv2009.0
+ Revision: 252760
- 3.2.14
- check harder if splash is disabled

* Fri Jul 25 2008 Olivier Blin <oblin@mandriva.com> 3.2.13-1mdv2009.0
+ Revision: 249734
- 3.2.13
- add support for splashy themes inclusion in ext2 initrd
  (used by One build process)

* Thu Jul 24 2008 Olivier Blin <oblin@mandriva.com> 3.2.12-1mdv2009.0
+ Revision: 245479
- 3.2.12
- set splashy theme when building bootsplash
- add splashy theme files if splashy is available

* Wed Jul 23 2008 Olivier Blin <oblin@mandriva.com> 3.2.11-1mdv2009.0
+ Revision: 244086
- 3.2.11 (build fixes)
- 3.2.10
- splashy support

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 3.2.9-2mdv2009.0
+ Revision: 220491
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 3.2.9-1mdv2008.1
+ Revision: 135856
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Oct 03 2007 Thierry Vignaud <tv@mandriva.org> 3.2.9-1mdv2008.0
+ Revision: 95085
- updated translations
- uming fits well against current theme (funda)

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 3.2.8-2mdv2008.0
+ Revision: 69426
- fix buildrequires for x86_64
- kill file require on perl-base


* Thu Mar 15 2007 Pixel <pixel@mandriva.com> 3.2.8-1mdv2007.1
+ Revision: 144392
- switch-themes: handle /boot/gfxmenu for grub
- switch-themes: handle /boot/gfxmenu for grub

* Mon Mar 05 2007 Olivier Blin <oblin@mandriva.com> 3.2.6-1mdv2007.1
+ Revision: 132851
- 3.2.6 (use hibernate config files if present for suspend)

* Thu Mar 01 2007 Pixel <pixel@mandriva.com> 3.2.5-1mdv2007.1
+ Revision: 130391
- Requires perl-Archive-Cpio for cpio-filter
- use cpio-filter to remove bootsplash from initrd without being root
  (useful for mkcd)

* Tue Feb 27 2007 Pixel <pixel@mandriva.com> 3.2.4-1mdv2007.1
+ Revision: 126445
- fix typo in make-boot-splash

* Mon Feb 26 2007 Pixel <pixel@mandriva.com> 3.2.3-1mdv2007.1
+ Revision: 125765
- create make-boot-splash-raw out of make-boot-splash
  (to be used by mkcd)

* Tue Feb 13 2007 Warly <warly@mandriva.com> 3.2.2-1mdv2007.1
+ Revision: 120360
- update tarball and spec for version 3.2.2
- update tarball and spec for version 3.2.2

* Mon Jan 22 2007 Olivier Blin <oblin@mandriva.com> 3.2.1-1mdv2007.1
+ Revision: 112060
- add suspend support in splash.sh

* Fri Dec 08 2006 Warly <warly@mandriva.com> 3.2.0-1mdv2007.1
+ Revision: 93848
- update tarball and spec for version 3.2.0
- Import bootsplash

* Wed Sep 06 2006 Warly <warly@mandriva.com> 3.1.13-1mdv2007.0
- added support for grub image in the theme

* Tue Apr 11 2006 Gwenole Beauchesne <gbeauchesne@mandriva.com> 3.1.12-1mdk
- Fix initramfs support (use cpio -c)

* Tue Apr 11 2006 Warly <warly@mandriva.com> 3.1.11-1mdk
- Do not require mkinitrd (mkinird will now prereq bootsplash)
- Handle initramfs in make-boot-splash and remove-boot-splash

* Sat Sep 17 2005 Pixel <pixel@mandriva.com> 3.1.10-1mdk
- fix upgrading mandrakelinux-theme to mandriva-theme by patching remove-theme
  ("remove-theme Mandrakelinux" from the preun of mandrakelinux-theme 
   will be called after the switch-theme from the post of mandriva-theme)
  this also implies mandriva-theme prereq this bootsplash

* Thu Sep 08 2005 Warly <warly@mandriva.com> 3.1.9-1mdk
- update po

* Fri Aug 12 2005 Nicolas Lécureuil <neoclust@mandriva.org> 3.1.8-2mdk
- fix url
- s/Mandrakelinux/Mandriva Linux/
- mkrel

* Fri Apr 08 2005 Warly <warly@mandrakesoft.com> 3.1.8-1mdk
- fix text mode

* Thu Apr 07 2005 Warly <warly@mandrakesoft.com> 3.1.7-1mdk
- Now fbmenu check that there are no duplicate entries

* Sat Apr 02 2005 Olivier Blin <oblin@mandrakesoft.com> 3.1.6-1mdk
- really try to get resolution from /dev/fb0
- fix BuildRequires
- from Pablo: translation updates

* Tue Mar 22 2005 Warly <warly@mandrakesoft.com> 3.1.5-1mdk
- Fix fbmenu compilation

* Thu Mar 17 2005 Warly <warly@mandrakesoft.com> 3.1.4-1mdk
- bootanim now uses bash getopts builtin

* Thu Mar 10 2005 Warly <warly@mandrakesoft.com> 3.1.3-1mdk
- now use libgtk-linux-fb-2.0-devel

* Fri Feb 18 2005 Warly <warly@mandrakesoft.com> 3.1.2-1mdk
- include fbmenu into the package

* Wed Feb 16 2005 Warly <warly@mandrakesoft.com> 3.1.1-1mdk
- improve fbmenu so that it can use fbgrab dump as background for the menu
- ad fbmenu for profiles menu
- include animations

* Tue Feb 08 2005 Pablo Saratxaga <pablo@mandrakesoft.com> 2.1.13-3mdk
- fixed Japanese display
- various new translations

* Fri Oct 01 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 2.1.13-2mdk
- fix rendering for UTF-8 in ttf.c and splash.sh
- removed copying of locale from post script (it is now done by DrakX/locale)
- various new translations

* Sat Sep 11 2004 Warly <warly@mandrakesoft.com> 2.1.13-1mdk
- Do not refresh the screen if we are in verbose mode when rc starts

* Thu Sep 09 2004 Warly <warly@mandrakesoft.com> 2.1.12-1mdk
- remove-theme now does not require an argument

* Wed Sep 01 2004 Warly <warly@mandrakesoft.com> 2.1.11-1mdk
- refresh the screen in non latin1 font with a separate /usr partition
- fix mngplay.static build

* Sat Jul 17 2004 Warly <warly@mandrakesoft.com> 2.1.9-1mdk
- fix rendering for UTF-8 mo (pablo)

* Fri Jul 02 2004 Olivier Blin <blino@mandrake.org> 2.1.8-1mdk
- fix bootloader-config path
- fix remove-boot-splash path
- from Pablo: added Urdu file

* Wed Jun 30 2004 Pixel <pixel@mandrakesoft.com> 2.1.7-1mdk
- add scripts/remove-boot-splash so we can modify a bootsplash 
  from an initrd without having to rebuild it
- make-boot-splash doesn't try to detect the resolution anymore,
  it now needs to be given one
- in switch-themes and remove-theme, use bootloader-config to update the bootloader
- remove detect-resolution
- requires new mkinitrd (old mkinitrd used detect-resolution)
- remove "Patch: glibc-fixed-header.tar.bz2" which is unused (and not in CVS)

* Wed Apr 28 2004 Warly <warly@mandrakesoft.com> 2.1.6-1mdk
- fix compilation

* Fri Mar 19 2004 Warly <warly@mandrakesoft.com> 2.1.5-1mdk
- add Olivier Blin fixes to handle symbolic link into detect-resolution

