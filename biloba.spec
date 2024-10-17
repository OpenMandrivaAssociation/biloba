Summary:	A tactical board game
Name:		biloba
Version:	0.9.3
Release:	3
License:	GPLv2+
Group:		Games/Boards
Url:		https://biloba.sourceforge.net/
Source0:	http://osdn.dl.sourceforge.net/sourceforge/biloba/%{name}-%{version}.tar.gz
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_mixer)

%description
Biloba is a very innovative tactical board game.
It can be played by 2, 3 or 4 players and against the computer (IA).
After installing the game you will be able to play on the same computer or
on-line against your opponents.

%files
%doc AUTHORS ChangeLog README
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/biloba.desktop
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png

#----------------------------------------------------------------------------

%prep
%setup -q
# fix linting
iconv -f iso8859-1 -t utf-8 ChangeLog > ChangeLog.conv && mv -f ChangeLog.conv ChangeLog

%build
%configure2_5x \
	--bindir=%{_bindir} \
	--datadir=%{_datadir}
%make

%install
%makeinstall bindir=%{buildroot}%{_bindir} \
	datadir=%{buildroot}%{_datadir}

# install menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=A tactical board game
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;BoardGame;
EOF

# install icons
mkdir -p %{buildroot}{%{_liconsdir},%{_miconsdir},%{_iconsdir}}
cp %{name}_icon.png %{buildroot}%{_liconsdir}/%{name}.png
convert -scale 32x32 %{name}_icon.png %{buildroot}%{_iconsdir}/%{name}.png
convert -scale 16x16 %{name}_icon.png %{buildroot}%{_miconsdir}/%{name}.png

