# TODO:
# - ipv6 support
#
# Conditional build:
%bcond_with	rogue	# with Rogue ("Ground Zero") Mission Pack  (non-distributable package)
%bcond_with	xatrix	# with Xatrix ("The Reckoning") Mission Pack  (non-distributable package)
#
Summary:	Quake2Forge - improved version of id Software's classic Quake II engine
Summary(pl.UTF-8):	Quake2Forge - ulepszona wersja klasycznego silnika Quake II firmy id Software
Name:		quake2forge
Version:	0.3
Release:	3
License:	GPL (for main code only)
Group:		Applications/Games
# http://dl.sourceforge.net/quake/quake2-%{version}.tar.gz [but no 0.3 yet]
# ftp://ftp.quakeforge.net/quake2forge/quake2-%{version}.tar.gz [dead]
Source0:	quake2-%{version}.tar.gz
# Source0-md5:	2c167ff7edce20f0240316b98a1e4515
#Source1:	multiplay pack (need to check licence)
# ftp://ftp.idsoftware.com/idstuff/quake2/q2-3.20-x86-full.exe
Source2:	%{name}-server.conf
Source3:	%{name}-server
Source4:	%{name}.png
Source5:	%{name}.desktop
Source6:	q2ded.sysconfig
Source7:	q2ded.screenrc
Source8:	%{name}-rogue.desktop
Source9:	%{name}-xatrix.desktop
Source10:	ftp://ftp.idsoftware.com/idstuff/quake2/source/roguesrc320.shar.Z
# Source10-md5:	7d5e052839c9e629bad0a6570aa70554
Source11:	ftp://ftp.idsoftware.com/idstuff/quake2/source/xatrixsrc320.shar.Z
# Source11-md5:	41fc4ecc4f25c068e7d1f488bd4a1e1a
Patch0:		%{name}-stupid_nvidia_bug.patch
Patch1:		%{name}-gl.patch
Patch2:		%{name}-ac.patch
Patch3:		%{name}-fix.patch
Patch4:		%{name}-gamedir.patch
Patch5:		%{name}-missionpacks.patch
Patch6:		%{name}-rogue-fix.patch
Patch7:		%{name}-xatrix-fix.patch
URL:		http://www.quakeforge.net/
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	SDL-devel
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	libao-devel >= 0.8.5
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	svgalib-devel
BuildRequires:	unzip
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXxf86dga-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
Requires:	%{name}-common = %{version}-%{release}
Requires:	%{name}-renderer = %{version}-%{release}
Obsoletes:	quake2 <= 1:0.3
Obsoletes:	quake2-static <= 1:0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gamelibdir	%{_libdir}/quake2
%define		_gamedatadir	%{_datadir}/quake2
%define		_gamehomedir	/var/games/quake2

# because of gl_image.c:1559
%define		specflags	-fno-strict-aliasing

%description
Quake2Forge - improved version of id Software's classic Quake II
engine.

%description -l pl.UTF-8
Quake2Forge - ulepszona wersja klasycznego silnika Quake II firmy id
Software.

%package common
Summary:	Quake2Forge common files
Group:		Applications/Games
Provides:	quake2-common

%description common
Quake2Forge common files.

%package server
Summary:	Quake2Forge server
Summary(pl.UTF-8):	Serwer Quake2Forge
Summary(pt_BR.UTF-8):	Servidor Quake2Forge
Group:		Applications/Games
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires:	%{name}-common = %{version}-%{release}
Requires:	rc-scripts
Requires:	screen
Provides:	group(quake2)
Provides:	user(quake2)
Obsoletes:	quake2-server <= 1:0.3

%description server
Quake2Forge server.

%description server -l pl.UTF-8
Serwer Quake2Forge dla Linuksa.

%description server -l pt_BR.UTF-8
Servidor Quake2Forge.

%package 3dfx
Summary:	Quake2Forge 3DFX libs
Summary(pl.UTF-8):	Biblioteki 3DFX dla Quake2Forge
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-renderer = %{version}-%{release}
Obsoletes:	quake2-3DFX
Obsoletes:	quake2-3dfx <= 1:0.3

%description 3dfx
Play Quake2Forge using 3DFX acceleration.

%description 3dfx -l pl.UTF-8
Zagraj w Quake2Forge z akceleracją 3DFX.

%package glx
Summary:	OpenGL Quake2Forge
Summary(pl.UTF-8):	Quake2Forge OpenGL
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-renderer = %{version}-%{release}
Obsoletes:	quake2-GLX
Obsoletes:	quake2-glx <= 1:0.3

%description glx
Play Quake2Forge using hardware OpenGL acceleration.

%description glx -l pl.UTF-8
Zagraj w Quake2Forge ze sprzętową akceleracją OpenGL.

%package sdl
Summary:	Quake2Forge for SDL
Summary(pl.UTF-8):	Biblioteki Quake2Forge dla SDL
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-renderer = %{version}-%{release}
Obsoletes:	quake2-sdl <= 1:0.3

%description sdl
Quake2Forge libraries for SDL play.

%description sdl -l pl.UTF-8
Biblioteki Quake2Forge do grania na SDL.

%package sgl
Summary:	Quake2Forge for SDL with GL
Summary(pl.UTF-8):	Biblioteki Quake2Forge dla SDL z obsługą GL
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-renderer = %{version}-%{release}
Obsoletes:	quake2-sgl <= 1:0.3

%description sgl
Quake2Forge libraries for SDL with GL play.

%description sgl -l pl.UTF-8
Biblioteki Quake2Forge do grania na SDL z obsługą GL.

%package svga
Summary:	Quake2Forge for SVGAlib
Summary(pl.UTF-8):	Biblioteki Quake2Forge dla SVGAlib
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-renderer = %{version}-%{release}
Obsoletes:	quake2-svga <= 1:0.3
Obsoletes:	quake2-svgalib

%description svga
Quake2Forge libraries for SVGAlib play.

%description svga -l pl.UTF-8
Biblioteki Quake2Forge do grania na SVGAlib.

%package x11
Summary:	Quake2Forge X11 software renderer libs
Summary(pl.UTF-8):	Biblioteka Quake2Forge - programowe renderowanie
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-renderer = %{version}-%{release}
Obsoletes:	quake2-X11
Obsoletes:	quake2-software-X11
Obsoletes:	quake2-x11 <= 1:0.3

%description x11
Play Quake2Forge using software X11 renderer.

%description x11 -l pl.UTF-8
Zagraj w Quake2Forge przy użyciu programowego renderowania w X11.

%package snd-alsa
Summary:	Quake2Forge ALSA sound plugin
Summary(pl.UTF-8):	Wtyczka dźwięku ALSA dla Quake2Forge
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound-plugin = %{version}-%{release}
Obsoletes:	quake2-snd-alsa <= 1:0.3

%description snd-alsa
ALSA sound plugin for Quake2Forge.

%description snd-alsa -l pl.UTF-8
Wtyczka dźwięku ALSA dla Quake2Forge.

%package snd-ao
Summary:	Quake2Forge ao sound plugin
Summary(pl.UTF-8):	Wtyczka dźwięku ao dla Quake2Forge
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound-plugin = %{version}-%{release}
Obsoletes:	quake2-snd-ao <= 1:0.3

%description snd-ao
Ao sound plugin for Quake2Forge.

%description snd-ao -l pl.UTF-8
Wtyczka dźwięku ao dla Quake2Forge.

%package snd-oss
Summary:	Quake2Forge OSS sound plugin
Summary(pl.UTF-8):	Wtyczka dźwięku OSS dla Quake2Forge
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound-plugin = %{version}-%{release}
Obsoletes:	quake2-snd-oss <= 1:0.3

%description snd-oss
OSS sound plugin for Quake2Forge.

%description snd-oss -l pl.UTF-8
Wtyczka dźwięku OSS dla Quake2Forge.

%package snd-sdl
Summary:	Quake2Forge SDL sound plugin
Summary(pl.UTF-8):	Wtyczka dźwięku SDL dla Quake2Forge
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound-plugin = %{version}-%{release}
Obsoletes:	quake2-snd-sdl <= 1:0.3

%description snd-sdl
SDL sound plugin for Quake2Forge.

%description snd-sdl -l pl.UTF-8
Wtyczka dźwięku SDL dla Quake2Forge.

%package rogue
Summary:	Quake2Forge: Ground Zero (mission pack)
Summary(pl.UTF-8):	Quake2Forge: Ground Zero (zestaw misji)
License:	GPL+Limited Program Source Code License (non-distributable in binary form)
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}

%description rogue
Quake2Forge: Ground Zero (mission pack).

%description rogue -l pl.UTF-8
Quake2Forge: Ground Zero (zestaw misji).

%package xatrix
Summary:	Quake2Forge: The Reckoning (mission pack)
Summary(pl.UTF-8):	Quake2Forge: The Reckoning (zestaw misji)
License:	GPL+Limited Program Source Code License (non-distributable in binary form)
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}

%description xatrix
Quake2Forge: The Reckoning (mission pack).

%description xatrix -l pl.UTF-8
Quake2Forge: The Reckoning (zestaw misji).

%prep
%setup -q -n quake2-%{version}
%patch0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%if %{with rogue}
cd src/rogue
gzip -dc %{SOURCE10} | %{__sed} s/"^more "/"cat >LICENSE.rogue "/ >rogue.shar
echo yes| sh rogue.shar
cd ../..
%patch6 -p1
%endif

%if %{with xatrix}
cd src/xatrix
gunzip -c %{SOURCE11} | %{__sed} s/"^more "/"cat >LICENSE.xatrix "/ >xatrix.shar
echo yes| sh xatrix.shar
cd ../..
%patch7 -p1
%endif

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	--disable-static \
%ifarch sparc sparcv9 sparc64
	--disable-warn \
%endif
	--enable-sdlsound

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_gamedatadir}/baseq2,%{_gamehomedir}/.quake2/baseq2} \
	$RPM_BUILD_ROOT{/etc/sysconfig,/etc/rc.d/init.d} \
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

install %{SOURCE2} $RPM_BUILD_ROOT%{_gamehomedir}/.quake2/baseq2/server.cfg
install %{SOURCE7} $RPM_BUILD_ROOT%{_gamehomedir}/.screenrc
install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/q2ded
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE5} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
install %{SOURCE6} $RPM_BUILD_ROOT/etc/sysconfig/q2ded

%if %{with rogue}
install %{SOURCE8} $RPM_BUILD_ROOT%{_desktopdir}/%{name}-rogue.desktop
%endif
%if %{with xatrix}
install %{SOURCE8} $RPM_BUILD_ROOT%{_desktopdir}/%{name}-xatrix.desktop
%endif

rm -rf _doc
cp -a docs _doc
rm -rf _doc/{CVS,Makefile*,ctf/CVS,ctf/Makefile*}

rm -f $RPM_BUILD_ROOT%{_gamelibdir}/*.la
rm -f $RPM_BUILD_ROOT%{_gamelibdir}/*/game.la
rm -f $RPM_BUILD_ROOT%{_gamedatadir}/baseq2/config.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%pre server
%groupadd -P %{name}-server -g 170 quake2
%useradd -P %{name}-server -u 170 -d %{_gamehomedir} -s /bin/sh -c "Quake 2" -g quake2 quake2

%post server
/sbin/chkconfig --add q2ded
%service q2ded restart "Quake2 server"

%preun server
if [ "$1" = "0" ]; then
	%service q2ded stop
	/sbin/chkconfig --del q2ded
fi

%postun server
if [ "$1" = "0" ]; then
	%userremove quake2
	%groupremove quake2
fi

%triggerpostun server -- quake2-server < 1:0.3-3.11
if [ -f %{_gamedatadir}/baseq2/server.cfg.rpmsave ]; then
	mv -f %{_gamehomedir}/.quake2/baseq2/server.cfg{,.rpmnew}
	mv -f %{_gamedatadir}/baseq2/server.cfg.rpmsave %{_gamehomedir}/.quake2/baseq2/server.cfg
fi

if [ -f /var/lock/subsys/quake2-server ]; then
	mv -f /var/lock/subsys/{quake2-server,q2ded}
	%service -q q2ded restart
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS HACKING README TODO _doc/*
%{_pixmapsdir}/quake2forge.png
%{_desktopdir}/quake2forge.desktop

%files common
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/quake2
%dir %{_gamelibdir}
%dir %{_gamelibdir}/baseq2
%dir %{_gamelibdir}/ctf
%attr(755,root,root) %{_gamelibdir}/baseq2/game.so
%attr(755,root,root) %{_gamelibdir}/ctf/game.so
#%%{_gamedir}/baseq2/pak2.pak
#%%{_gamedir}/baseq2/players
%dir %{_gamedatadir}
%dir %{_gamedatadir}/baseq2

%files server
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/q2ded
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/q2ded
%dir %attr(770,root,quake2) %{_gamehomedir}
%config(noreplace) %attr(660,root,quake2) %verify(not md5 mtime size) %{_gamehomedir}/.screenrc
%dir %attr(770,root,quake2) %{_gamehomedir}/.quake2
%dir %attr(770,root,quake2) %{_gamehomedir}/.quake2/baseq2
%config(noreplace) %attr(660,root,quake2) %verify(not md5 mtime size) %{_gamehomedir}/.quake2/baseq2/server.cfg

%files 3dfx
%defattr(644,root,root,755)
%attr(755,root,root) %{_gamelibdir}/ref_tdfx.so

%files glx
%defattr(644,root,root,755)
%attr(755,root,root) %{_gamelibdir}/ref_glx.so

%files sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_gamelibdir}/ref_softsdl.so

%files sgl
%defattr(644,root,root,755)
%attr(755,root,root) %{_gamelibdir}/ref_sdlgl.so

%files svga
%defattr(644,root,root,755)
%attr(755,root,root) %{_gamelibdir}/ref_soft.so

%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_gamelibdir}/ref_softx.so

%files snd-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_gamelibdir}/snd_alsa.so

%files snd-ao
%defattr(644,root,root,755)
%attr(755,root,root) %{_gamelibdir}/snd_ao.so

%files snd-oss
%defattr(644,root,root,755)
%attr(755,root,root) %{_gamelibdir}/snd_oss.so

%files snd-sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_gamelibdir}/snd_sdl.so

%if %{with rogue}
%files rogue
%defattr(644,root,root,755)
%doc src/rogue/LICENSE.rogue
%dir %{_gamelibdir}/rogue
%attr(755,root,root) %{_gamelibdir}/rogue/game.so
%{_desktopdir}/quake2forge-rogue.desktop
%endif

%if %{with xatrix}
%files xatrix
%defattr(644,root,root,755)
%doc src/xatrix/LICENSE.xatrix
%dir %{_gamelibdir}/xatrix
%attr(755,root,root) %{_gamelibdir}/xatrix/game.so
%{_desktopdir}/quake2forge-xatrix.desktop
%endif
