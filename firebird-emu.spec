%global commit1 8cb648fb02d3f18fb7f325cbe71bbb0a56a0bbe7
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})

Name:           firebird-emu
Version:        1.6
Release:        2%{?dist}
Summary:        Third-party emulator for ARM-based TI calculators

License:        GPLv3 and Public Domain
URL:            https://github.com/nspire-emus/firebird
Source0:        %url/archive/v%{version}/firebird-%{version}.tar.gz

# Bundled gif-h as submodule.
Source1:        https://github.com/jacobly0/gif-h/archive/%{commit1}.tar.gz#/gif-h-%{shortcommit1}.tar.gz

BuildRequires:  gcc, gcc-c++
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtquickcontrols2-devel
BuildRequires:  zlib-devel
BuildRequires:  desktop-file-utils

Requires:       hicolor-icon-theme

# Bundled copy of gif-h, an unversioned, one-file header-only C++ library
# that was forked by the firebird-emu developers.
# There is no version, so just use YYYYMMDD.revision.
Provides:       bundled(gif-h) = 20180321.%{commit1}

# Exclude some architectures.
# https://github.com/nspire-emus/firebird/issues/127
# ppc64le fails on Rawhide now, but aarch64 is fixed:
# https://github.com/nspire-emus/firebird/issues/196
ExcludeArch:    ppc64 i686 ppc64le

%description
This project is the community, third-party TI Nspire emulator,
Texas Instruments' ARM-based series of graphing calculators.
It supports the emulation of Touchpad, CX and CX CAS calcs on
Android, iOS, Linux, Mac and Windows.

%prep
%autosetup -n firebird-%{version}

# Fix up desktop file.
sed 's/DesktopUtility/X-DesktopUtility/g' -i resources/org.firebird-emus.firebird-emu.desktop

# Install gif-h submodule from source1 tarball.
cd core/
rm -rf gif-h/
tar xfz %SOURCE1
mv gif-h-%{commit1} gif-h

%build
%qmake_qt5  PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

# Validate desktop file.
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.firebird-emus.firebird-emu.desktop

%files
%license LICENSE
%doc README.md TODO.md
%{_bindir}/firebird-emu
%{_bindir}/firebird-send
%{_datadir}/applications/org.firebird-emus.firebird-emu.desktop
%{_datadir}/icons/hicolor/*/apps/org.firebird-emus.firebird-emu.png

%changelog
* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Apr 01 2023 Leigh Scott <leigh123linux@gmail.com> - 1.6-1
- Updated to latest upstream release.

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 02 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 17 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 21 2020 Ben Rosser <rosser.bjr@gmail.com> - 1.5-1
- Updated to latest upstream release.

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 Ben Rosser <rosser.bjr@gmail.com> - 1.4-1
- Update to latest release.

* Mon Feb  6 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.2-1
- Initial package for Fedora.
