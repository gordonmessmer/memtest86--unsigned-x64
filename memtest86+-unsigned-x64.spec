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

License:        GPLv2
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc
BuildRequires:  make

%description
Memtest86+ is a stand-alone memory tester for x86 and x86-64 architecture
computers. It provides a more thorough memory check than that provided by
BIOS memory tests.

%prep
%autosetup -n memtest86plus-%{version}


%build
cd build64
%make_build


%install
cd build64
mkdir -p %{buildroot}/{boot,%{efi_esp_dir}}
install -m 0644 memtest.efi %{buildroot}/%{efi_esp_dir}/memtest.efi
install -m 0644 memtest.bin %{buildroot}/boot/memtest.bin


%files
%license LICENSE
%doc README.md
%{efi_esp_dir}/memtest.efi
/boot/memtest.bin


%changelog
* Thu Jan 26 2023 Gordon Messmer <gordon.messmer@gmail.com>
- Initial package
