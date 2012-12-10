%define name biloba
%define version 0.6
%define release %mkrel 2

Summary: A tactical board game
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://osdn.dl.sourceforge.net/sourceforge/biloba/%{name}-%{version}.tar.gz
License: GPLv2+
Group:  Games/Boards
Url: 	http://biloba.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: SDL_image-devel
BuildRequires: SDL-devel
BuildRequires: imagemagick
BuildRequires: SDL_mixer-devel 
%description
Biloba is a very innovative tactical board game. 
It can be played by 2, 3 or 4 players and against the computer (IA). 
After installing the game you will be able to play on the same computer or 
online against your opponents.

%prep
%setup -q

%build
%configure --bindir=%{_gamesbindir} --datadir=%{_gamesdatadir}
%make

%install
rm -rf %{buildroot}
%makeinstall bindir=%{buildroot}%{_gamesbindir} \
	datadir=%{buildroot}%{_gamesdatadir}

# install menu

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=A tactical board game
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Games-Boards;Game;BoardGame;
EOF

# install icons
mkdir -p %{buildroot}{%{_liconsdir},%{_miconsdir},%{_iconsdir}}
cp %{name}_icon.png %{buildroot}%{_liconsdir}/%{name}.png
convert -scale 32x32 %{name}_icon.png %{buildroot}%{_iconsdir}/%{name}.png
convert -scale 16x16 %{name}_icon.png $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif


%files
%defattr(-,root,root)
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_liconsdir}/%name.png
%{_miconsdir}/%name.png
%{_iconsdir}/%name.png
%{_datadir}/applications/mandriva-biloba.desktop
%doc AUTHORS ChangeLog README



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6-2mdv2011.0
+ Revision: 616755
- the mass rebuild of 2010.0 packages

* Tue Jun 09 2009 J√©r√¥me Brenier <incubusss@mandriva.org> 0.6-1mdv2010.0
+ Revision: 384539
- use gamesbindir and gamesdatadir
- update to new version 0.6
- fix desktop file
- fix license
- add doc
- clean spec file

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.4-7mdv2009.0
+ Revision: 243285
- rebuild
- drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.4-5mdv2008.1
+ Revision: 135829
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Sep 01 2006 Nicolas L√©cureuil <neoclust@mandriva.org>
+ 2006-09-01 17:02:16 (59381)
- Fix File List

* Fri Sep 01 2006 Nicolas L√©cureuil <neoclust@mandriva.org>
+ 2006-09-01 14:55:27 (59330)
- XDG

* Thu Aug 03 2006 Nicolas L√©cureuil <neoclust@mandriva.org>
+ 2006-08-03 09:44:11 (43092)
- import biloba-0.4-3mdk

* Tue Dec 27 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.4-3mdk
- Fix file section

* Mon Oct 17 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.4-2mdk
- Fix BuildRequires now they are x86_64 friendly

* Mon Oct 17 2005 Erwan Velu <erwan@seanodes.com> 0.4-1mdk
- 0.4

* Fri Sep 30 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.3-3mdk
- Fix BuildRequires

* Thu Sep 29 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.3-2mdk
- Fix menu entry  group != menu

* Tue Sep 27 2005 Erwan Velu <erwan@seanodes.com> 0.3-1mdk
- 0.3
- Adding menu entry

* Fri Sep 23 2005 Erwan Velu <erwan@seanodes.com> 0.2-1mdk
- initial release

