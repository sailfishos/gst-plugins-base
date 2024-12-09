%define majorminor  1.0
%define gstreamer   gstreamer

%global _vpath_srcdir subprojects/gst-plugins-base
%global _vpath_builddir subprojects/gst-plugins-base/_build

Name:		%{gstreamer}%{majorminor}-plugins-base
Version:	1.24.10
Release:	1
Summary:	GStreamer streaming media framework base plug-ins
License:	LGPLv2+
URL:		http://gstreamer.freedesktop.org/
Source:		%{name}-%{version}.tar.xz

%define sonamever %(echo %{version} | cut -d '+' -f 1)

Requires:      orc >= 0.4.18
BuildRequires: pkgconfig(gstreamer-1.0) >= %{sonamever}
BuildRequires: gstreamer1.0-tools
BuildRequires: pkgconfig(orc-0.4) >= 0.4.18
BuildRequires: pkgconfig(ogg)
BuildRequires: pkgconfig(vorbis)
BuildRequires: pkgconfig(theora)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(opus)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(wayland-protocols) >= 1.15
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(iso-codes)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: meson
BuildRequires: gettext-devel

%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

%package devel
Summary:	GStreamer Plugin Library Headers
Requires:	%{gstreamer}1.0-plugins-base = %{version}

%description devel
GStreamer Plugins Base library development and header files.

%package apps
Summary:	GStreamer Plugins Base library applications
Requires:	%{gstreamer}1.0-plugins-base = %{version}

%description apps
GStreamer Plugins Base library applications

%prep
%autosetup -p1 -n gstreamer1.0-plugins-base-%{version}/gstreamer

%build

%meson \
  -Dpackage-name='SailfishOS GStreamer package plugins (base set)' \
  -Dpackage-origin='http://sailfishos.org/' \
  -Dexamples=disabled \
  -Ddebugutils=disabled \
  -Ddoc=disabled \
  -Ddsd=disabled \
  -Dintrospection=enabled \
  -Dorc=enabled \
  -Dopus=enabled \
  -Dgl=enabled \
  -Dgl_api=gles2 \
  -Dgl_platform=egl \
  -Dgl_winsys=wayland \
  -Dnls=disabled \
  -Dalsa=disabled \
  -Dx11=disabled \
  -Dxvideo=disabled \
  -Dxshm=disabled \
  -Dcdparanoia=disabled \
  -Dlibvisual=disabled \
  -Dgl-graphene=disabled \
  -Dtremor=disabled

%meson_build

%install
%meson_install

# Clean out files that should not be part of the rpm.
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -fr $RPM_BUILD_ROOT%{_datadir}/gst-plugins-base/1.0/license-translations.dict
rm -fr $RPM_BUILD_ROOT%{_mandir}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig

%files
%license subprojects/gst-plugins-base/COPYING
%{_libdir}/libgstallocators-%{majorminor}.so.*
%{_libdir}/libgstapp-%{majorminor}.so.*
%{_libdir}/libgstaudio-%{majorminor}.so.*
%{_libdir}/libgstfft-%{majorminor}.so.*
%{_libdir}/libgstgl-%{majorminor}.so.*
%{_libdir}/libgstpbutils-%{majorminor}.so*
%{_libdir}/libgstriff-%{majorminor}.so.*
%{_libdir}/libgstrtp-%{majorminor}.so*
%{_libdir}/libgstrtsp-%{majorminor}.so.*
%{_libdir}/libgstsdp-%{majorminor}.so.*
%{_libdir}/libgsttag-%{majorminor}.so.*
%{_libdir}/libgstvideo-%{majorminor}.so.*
%{_libdir}/gstreamer-%{majorminor}/libgstadder.so
%{_libdir}/gstreamer-%{majorminor}/libgstapp.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudioconvert.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiomixer.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiorate.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudioresample.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiotestsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstcompositor.so
%{_libdir}/gstreamer-%{majorminor}/libgstencoding.so
%{_libdir}/gstreamer-%{majorminor}/libgstgio.so
%{_libdir}/gstreamer-%{majorminor}/libgstogg.so
%{_libdir}/gstreamer-%{majorminor}/libgstopengl.so
%{_libdir}/gstreamer-%{majorminor}/libgstopus.so
%{_libdir}/gstreamer-%{majorminor}/libgstoverlaycomposition.so
%{_libdir}/gstreamer-%{majorminor}/libgstpango.so
%{_libdir}/gstreamer-%{majorminor}/libgstpbtypes.so
%{_libdir}/gstreamer-%{majorminor}/libgstplayback.so
%{_libdir}/gstreamer-%{majorminor}/libgstrawparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstsubparse.so
%{_libdir}/gstreamer-%{majorminor}/libgsttcp.so
%{_libdir}/gstreamer-%{majorminor}/libgsttheora.so
%{_libdir}/gstreamer-%{majorminor}/libgsttypefindfunctions.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideoconvertscale.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideorate.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideotestsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstvolume.so
%{_libdir}/gstreamer-%{majorminor}/libgstvorbis.so
%{_libdir}/girepository-1.0/GstAllocators-1.0.typelib
%{_libdir}/girepository-1.0/GstApp-1.0.typelib
%{_libdir}/girepository-1.0/GstAudio-1.0.typelib
%{_libdir}/girepository-1.0/GstGL-1.0.typelib
%{_libdir}/girepository-1.0/GstGLEGL-1.0.typelib
%{_libdir}/girepository-1.0/GstGLWayland-1.0.typelib
%{_libdir}/girepository-1.0/GstPbutils-1.0.typelib
%{_libdir}/girepository-1.0/GstRtp-1.0.typelib
%{_libdir}/girepository-1.0/GstRtsp-1.0.typelib
%{_libdir}/girepository-1.0/GstSdp-1.0.typelib
%{_libdir}/girepository-1.0/GstTag-1.0.typelib
%{_libdir}/girepository-1.0/GstVideo-1.0.typelib

%files devel
%{_includedir}/gstreamer-%{majorminor}/gst/allocators/*.h
%{_includedir}/gstreamer-%{majorminor}/gst/app/*.h
%{_includedir}/gstreamer-%{majorminor}/gst/audio/*.h
%{_includedir}/gstreamer-%{majorminor}/gst/fft/*.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/egl/*.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/glprototypes/*.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/*.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/wayland/*.h
%{_includedir}/gstreamer-%{majorminor}/gst/pbutils/*.h
%{_includedir}/gstreamer-%{majorminor}/gst/riff/*.h
%{_includedir}/gstreamer-%{majorminor}/gst/rtp/*.h
%{_includedir}/gstreamer-%{majorminor}/gst/rtsp/*.h
%{_includedir}/gstreamer-%{majorminor}/gst/sdp/*.h
%{_includedir}/gstreamer-%{majorminor}/gst/tag/*.h
%{_includedir}/gstreamer-%{majorminor}/gst/video/*.h
%{_libdir}/gstreamer-%{majorminor}/include/gst/gl/gstglconfig.h
%{_libdir}/libgstallocators-%{majorminor}.so
%{_libdir}/libgstapp-%{majorminor}.so
%{_libdir}/libgstaudio-%{majorminor}.so
%{_libdir}/libgstfft-%{majorminor}.so
%{_libdir}/libgstgl-%{majorminor}.so
%{_libdir}/libgstpbutils-%{majorminor}.so
%{_libdir}/libgstriff-%{majorminor}.so
%{_libdir}/libgstrtp-%{majorminor}.so
%{_libdir}/libgstrtsp-%{majorminor}.so
%{_libdir}/libgstsdp-%{majorminor}.so
%{_libdir}/libgsttag-%{majorminor}.so
%{_libdir}/libgstvideo-%{majorminor}.so
%{_libdir}/pkgconfig/gstreamer-allocators-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-app-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-audio-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-fft-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-gl-egl-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-gl-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-gl-prototypes-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-gl-wayland-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-pbutils-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-plugins-base-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-riff-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-rtp-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-rtsp-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-sdp-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-tag-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-video-%{majorminor}.pc
%{_datadir}/gir-1.0/GstAllocators-1.0.gir
%{_datadir}/gir-1.0/GstApp-1.0.gir
%{_datadir}/gir-1.0/GstAudio-1.0.gir
%{_datadir}/gir-1.0/GstGL-1.0.gir
%{_datadir}/gir-1.0/GstGLEGL-1.0.gir
%{_datadir}/gir-1.0/GstGLWayland-1.0.gir
%{_datadir}/gir-1.0/GstPbutils-1.0.gir
%{_datadir}/gir-1.0/GstRtp-1.0.gir
%{_datadir}/gir-1.0/GstRtsp-1.0.gir
%{_datadir}/gir-1.0/GstSdp-1.0.gir
%{_datadir}/gir-1.0/GstTag-1.0.gir
%{_datadir}/gir-1.0/GstVideo-1.0.gir

%files apps
%{_bindir}/gst-device-monitor-%{majorminor}
%{_bindir}/gst-discoverer-%{majorminor}
%{_bindir}/gst-play-%{majorminor}
