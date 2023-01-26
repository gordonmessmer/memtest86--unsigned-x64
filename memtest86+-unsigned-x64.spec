# Prevent stripping
%global __spec_install_post /usr/lib/rpm/brp-compress
# Turn off debuginfo package
%global debug_package %{nil}
%global forgeurl https://github.com/memtest86plus/memtest86plus

Name:           memtest86+-unsigned-x64
Version:        6.01
Release:        1%{?dist}
Summary:        Stand-alone memory tester for x86 and x86-64 architecture computers
%forgemeta

License:        GPLv2 and GPLv3
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        20_memtest86+

BuildRequires:  gcc
BuildRequires:  make
ExclusiveArch:  x86_64

%description
Memtest86+ is a stand-alone memory tester for x86 and x86-64 architecture
computers. It provides a more thorough memory check than that provided by
BIOS memory tests.

%package efi
Summary: EFI version of memtest86+
Requires: %{name}%{?_isa} = %{version}-%{release}


%description efi
memtest86+ is a stand-alone memory tester for x86 and x86-64 architecture
computers.

This package provides the EFI version of memtest86+.


%package bios
Summary: BIOS version of memtest86+
Requires: %{name}%{?_isa} = %{version}-%{release}


%description bios
memtest86+ is a stand-alone memory tester for x86 and x86-64 architecture
computers.

This package provides the BIOS version of memtest86+.


%prep
%autosetup -n memtest86plus-%{version}


%build
cd build64
# Regular build flags are not wanted for this binary
make


%install
cd build64
mkdir -p %{buildroot}/{boot,%{efi_esp_dir}}
install -m 0644 memtest.efi %{buildroot}/%{efi_esp_dir}/memtest.efi
install -m 0644 memtest.bin %{buildroot}/boot/memtest.bin

mkdir -p %{buildroot}%{_sysconfdir}/grub.d
install -m755 %{SOURCE1} %{buildroot}%{_sysconfdir}/grub.d

%files
%license LICENSE
%doc README.md


%files efi
%{efi_esp_dir}/memtest.efi


%files bios
%{_sysconfdir}/grub.d/20_memtest86+
/boot/memtest.bin


%changelog
* Thu Jan 26 2023 Gordon Messmer <gordon.messmer@gmail.com>
- Initial package
