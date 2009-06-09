%define name biloba
%define version 0.6
%define release %mkrel 1

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

