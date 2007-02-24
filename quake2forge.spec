# TODO:
# - ipv6 support
Summary:	Quake2 for linux
Summary(pl.UTF-8):	Quake2 dla Linuksa
Summary(pt_BR.UTF-8):	Quake2 para Linux
Name:		quake2
Version:	0.3
Release:	3.11
Epoch:		1
License:	GPL (for code only)
Group:		X11/Applications/Games
Source0:	ftp://ftp.quakeforge.net/quake2forge/%{name}-%{version}.tar.gz
# Source0-md5:	2c167ff7edce20f0240316b98a1e4515
#Source1:	multiplay pack (need to check licence)
# ftp://ftp.idsoftware.com/idstuff/quake2/q2-3.20-x86-full.exe
Source2:	%{name}-server.conf
Source3:	%{name}-server
Source4:	%{name}.png
Source5:	%{name}.desktop
Source6:	q2ded.sysconfig
Source7:	q2ded.screenrc
Patch0:		%{name}-stupid_nvidia_bug.patch
Patch1:		%{name}-gl.patch
URL:		http://www.quakeforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libao-devel >= 0.8.5
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sed >= 4.0
BuildRequires:	svgalib-devel
BuildRequires:	unzip
Requires:	%{name}-renderer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gamelibdir	%{_libdir}/games/%{name}
%define		_gamedatadir	%{_datadir}/games/%{name}
%define		_gamehomedir	/var/games/%{name}

%description
Quake2 for linux!

%description -l pl.UTF-8
Quake2 dla Linuksa!

%description -l pt_BR.UTF-8
Quake2 para Linux!

%package server
Summary:	Quake2 server
Summary(pl.UTF-8):	Serwer Quake2
Summary(pt_BR.UTF-8):	Servidor Quake2
Group:		Applications/Games
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	rc-scripts
Requires:	screen
Provides:	group(quake2)
Provides:	user(quake2)

%description server
Quake2 server.

%description server -l pl.UTF-8
Serwer Quake2 dla Linuksa.

%description server -l pt_BR.UTF-8
Servidor Quake2.

%package 3dfx
Summary:	Quake2 3DFX libs
Summary(pl.UTF-8):	Biblioteki 3DFX dla Quake2
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	%{name}-renderer
Obsoletes:	quake2-3DFX

%description 3dfx
Play Quake2 using 3DFX acceleration.

%description 3dfx -l pl.UTF-8
Zagraj w Quake2 z akceleracją 3DFX.

%package glx
Summary:	OpenGL Quake2
Summary(pl.UTF-8):	Quake2 OpenGL
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	OpenGL
Provides:	%{name}-renderer
Obsoletes:	quake2-GLX

%description glx
Play Quake2 using hardware OpenGL acceleration.

%description glx -l pl.UTF-8
Zagraj w Quake2 ze sprzętową akceleracją OpenGL.

%package sdl
Summary:	Quake2 for SDL
Summary(pl.UTF-8):	Biblioteki Quake2 dla SDL
Group:		Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	%{name}-renderer

%description sdl
Quake2 libraries for SDL play.

%description sdl -l pl.UTF-8
Biblioteki Quake2 do grania na SDL.

%package sgl
Summary:	Quake2 for SDL with GL
Summary(pl.UTF-8):	Biblioteki Quake2 dla SDL z obsługą GL
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	%{name}-renderer

%description sgl
Quake2 libraries for SDL with GL play.

%description sgl -l pl.UTF-8
Biblioteki Quake2 do grania na SDL z obsługą GL.

%package svga
Summary:	Quake2 for SVGAlib
Summary(pl.UTF-8):	Biblioteki Quake2 dla SVGAlib
Group:		Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	%{name}-renderer
Obsoletes:	quake2-svgalib

%description svga
Quake2 libraries for SVGAlib play.

%description svga -l pl.UTF-8
Biblioteki Quake2 do grania na SVGAlib.

%package x11
Summary:	Quake2 X11 software renderer libs
Summary(pl.UTF-8):	Biblioteka Quake2 - programowe renderowanie
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	%{name}-renderer
Obsoletes:	quake2-X11
Obsoletes:	quake2-software-X11

%description x11
Play Quake2 using software X11 renderer.

%description x11 -l pl.UTF-8
Zagraj w Quake2 przy użyciu programowego renderowania w X11.

%package snd-oss
Summary:	Quake2 OSS sound plugin
Summary(pl.UTF-8):	Wtyczka dźwięku OSS dla Quake2
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	%{name}-sound-plugin

%description snd-oss
OSS sound plugin for Quake2.

%description -l pl.UTF-8
Wtyczka dźwięku OSS dla Quake2.

%package snd-sdl
Summary:	Quake2 SDL sound plugin
Summary(pl.UTF-8):	Wtyczka dźwięku SDL dla Quake2
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	%{name}-sound-plugin

%description snd-sdl
SDL sound plugin for Quake2.

%description -l pl.UTF-8
Wtyczka dźwięku SDL dla Quake2.

%package snd-alsa
Summary:	Quake2 ALSA sound plugin
Summary(pl.UTF-8):	Wtyczka dźwięku ALSA dla Quake2
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	%{name}-sound-plugin

%description snd-alsa
ALSA sound plugin for Quake2.

%description -l pl.UTF-8
Wtyczka dźwięku ALSA dla Quake2.

%package snd-ao
Summary:	Quake2 ao sound plugin
Summary(pl.UTF-8):	Wtyczka dźwięku ao dla Quake2
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	%{name}-sound-plugin

%description snd-ao
Ao sound plugin for Quake2.

%description -l pl.UTF-8
Wtyczka dźwięku ao dla Quake2.

%prep
%setup -q
%patch0
%patch1 -p1

%{__sed} -i -e 's/libltdl//' Makefile.am
%{__sed} -i -e 's/AC_LIBLTDL_CONVENIENCE/AC_LIBLTDL_INSTALLABLE/' configure.in

%build
%{__aclocal}
%{__autoheader}
%{__libtoolize} --ltdl --automake
%{__automake}
%{__autoconf}

%configure \
	--disable-static \
	--enable-ltdl-install=no \
	--libdir=%{_libdir}/games \
	--datadir=%{_datadir}/games \
	--enable-sdlsound \
	--with-opengl=/usr/X11R6

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_gamedatadir}/baseq2,%{_gamehomedir}/.quake2/baseq2} \
	$RPM_BUILD_ROOT{/etc/sysconfig,/etc/rc.d/init.d} \
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

#$RPM_BUILD_ROOT%{_gamedir}/baseq2/players/{crakhor,cyborg,female,male}

#for i in crakhor cyborg female male ; do
#        install baseq2/players/$i/* $RPM_BUILD_ROOT%{_gamedir}/baseq2/players/$i
#done
#install baseq2/pak2.pak        $RPM_BUILD_ROOT%{_gamedir}/quake2/baseq2

install %{SOURCE2} $RPM_BUILD_ROOT%{_gamehomedir}/.quake2/baseq2/server.cfg
install %{SOURCE7} $RPM_BUILD_ROOT%{_gamehomedir}/.screenrc
install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/q2ded
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE5} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
install %{SOURCE6} $RPM_BUILD_ROOT/etc/sysconfig/q2ded

rm -rf _doc
cp -a docs _doc
rm -rf _doc/{CVS,Makefile*,ctf/CVS,ctf/Makefile*}

rm -f $RPM_BUILD_ROOT%{_libdir}/games/quake2/snd_{alsa,ao,oss,sdl}.la
rm -f $RPM_BUILD_ROOT%{_libdir}/games/quake2/ref_{soft,softx,sdlgl,softsdl,glx}.la
rm -f $RPM_BUILD_ROOT%{_libdir}/games/quake2/{baseq2,ctf}/game.la
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

%triggerpostun server -- %{name}-server < 1:0.3-3.11
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
%{_pixmapsdir}/quake2.png
%{_desktopdir}/quake2.desktop

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
%{_gamelibdir}/ref_tdfx.la

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

%files snd-oss
%defattr(644,root,root,755)
%attr(755,root,root) %{_gamelibdir}/snd_oss.so

%files snd-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_gamelibdir}/snd_alsa.so

%files snd-ao
%defattr(644,root,root,755)
%attr(755,root,root) %{_gamelibdir}/snd_ao.so

%files snd-sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_gamelibdir}/snd_sdl.so
