%define name biloba
%define version 0.4
%define release %mkrel 7

Summary: A tactical board game
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://osdn.dl.sourceforge.net/sourceforge/biloba/%{name}-%{version}.tar.bz2
License: GPL
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
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

# install menu

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
iComment=A tactical board game
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Games-Boards;Game;BoardGame;
EOF

# install icons
mkdir -p $RPM_BUILD_ROOT{%{_liconsdir},%{_miconsdir},%{_iconsdir}}
cp %{name}_icon.png $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
convert -scale 32x32 %{name}_icon.png $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
convert -scale 16x16 %{name}_icon.png $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

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
%{_bindir}/biloba
%{_datadir}/biloba
%{_liconsdir}/%name.png
%{_miconsdir}/%name.png
%{_iconsdir}/%name.png
%{_datadir}/applications/mandriva-biloba.desktop


