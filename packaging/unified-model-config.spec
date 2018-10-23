%define debug_package %{nil}

Name:		unified-model-config
Summary:	All Model configurations
Version:	0.0.5
Release:	0
Group:		System/Configuration
BuildArch:	noarch
License:	Apache-2.0
Source0:	%{name}-%{version}.tar.gz
Source1001:	%{name}.manifest

%description
Model configuration data package

%package -n model-config-emulator-profile_common
Summary:	A Model configuration for common profile
Provides:	model-config
%description -n model-config-emulator-profile_common
Model configuiration data pacakge (emulator/common)

%package -n model-config-emulator-profile_mobile
Summary:	A Model configuration for mobile profile
Provides:	model-config
%description -n model-config-emulator-profile_mobile
Model configuiration data pacakge (emulator/mobile)

%package -n model-config-emulator-profile_wearable
Summary:	A Model configuration for wearable profile
Provides:	model-config
%description -n model-config-emulator-profile_wearable
Model configuiration data pacakge (emulator/wearable)

%package -n model-config-emulator-profile_tv
Summary:	A Model configuration for tv profile
Provides:	model-config
%description -n model-config-emulator-profile_tv
Model configuiration data pacakge (emulator/tv)

%package -n model-config-generic
Summary:	A Model configuration
Provides:	model-config
%description -n model-config-generic
Model configuration data package

%package -n model-config-default
Summary:	Default Model configuration for IoT
Provides:	model-config
%description -n model-config-default
Model configuration data package main body having default values for Tizen IOT

%package -n model-config-tm1
Summary:	A Model configuration for tm1
Provides:	model-config
%description -n model-config-tm1
Model configuiration data pacakge(tm1)

%package -n model-config-n4
Summary:	A Model configuration for tm2
Provides:	model-config
%description -n model-config-n4
Model configuiration data pacakge(tm2)

%package -n model-config-tw2
Summary:	A Model configuration for tw2
Provides:	model-config
%description -n model-config-tw2
Model configuiration data pacakge(tw2)

%package -n model-config-xu3-profile_common
Summary:	Model configuration of XU3 for common profiles
Provides:	model-config
%description -n model-config-xu3-profile_common
Model configuration data package main body supporting common profiles

%package -n model-config-xu3-profile_tv
Summary:	Model configuration of XU3 for TV profile
Provides:	model-config
%description -n model-config-xu3-profile_tv
Model configuration data package main body supporting TV profile

%package -n model-config-rpi3-profile_common
Summary:	Model configuration of RPi3 for common profile
Provides:	model-config
%description -n model-config-rpi3-profile_common
Model configuration data package main body supporting common profile

%package -n model-config-rpi3-profile_tv
Summary:	Model configuration of RPi3 for TV profile
Provides:	model-config
%description -n model-config-rpi3-profile_tv
Model configuration data package main body supporting TV profile


%prep
%setup -q -n %{name}-%{version}
cp %{SOURCE1001} ./%{name}.manifest

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/config

###### For emulator ######
cp -f emulator/model-config.xml %{buildroot}%{_sysconfdir}/config/emul_common.xml
cp -f emulator/model-config_wearable.xml %{buildroot}%{_sysconfdir}/config/emul_wearable.xml

%ifarch x86_64
cp -f emulator/model-config_tv64.xml %{buildroot}%{_sysconfdir}/config/emul_tv.xml
cp -f emulator/model-config_mobile64.xml %{buildroot}%{_sysconfdir}/config/emul_mobile.xml
%else
cp -f emulator/model-config_tv.xml %{buildroot}%{_sysconfdir}/config/emul_tv.xml
cp -f emulator/model-config_mobile.xml %{buildroot}%{_sysconfdir}/config/emul_mobile.xml
%endif

###### For generic ######
cp -f generic/model-config.xml %{buildroot}%{_sysconfdir}/config/generic.xml
cp -f generic/model-config-iot.xml %{buildroot}%{_sysconfdir}/config/iot.xml

###### For tm1 ######
cp -f tm1/model-config.xml %{buildroot}%{_sysconfdir}/config/tm1.xml

###### For tm2 ######
cp -f tm2/model-config.xml %{buildroot}%{_sysconfdir}/config/tm2.xml

###### For tw2 ######
cp -f tw2/model-config.xml %{buildroot}%{_sysconfdir}/config/tw2.xml

###### For xu3 ######
cp -f xu3/model-config.xml %{buildroot}%{_sysconfdir}/config/xu3.xml
cp -f xu3/model-config_tv.xml %{buildroot}%{_sysconfdir}/config/xu3_tv.xml

###### For rpi3 ######
cp -f rpi3/model-config.xml %{buildroot}%{_sysconfdir}/config/rpi3.xml
cp -f rpi3/model-config_tv.xml %{buildroot}%{_sysconfdir}/config/rpi3_tv.xml


%post -n model-config-emulator-profile_common
ln -sf emul_common.xml %{_sysconfdir}/config/model-config.xml
%files -n model-config-emulator-profile_common
%manifest %{name}.manifest
%config %{_sysconfdir}/config/emul_common.xml
%license LICENSE.Apache-2.0

%post -n model-config-emulator-profile_mobile
ln -sf emul_mobile.xml %{_sysconfdir}/config/model-config.xml
%files -n model-config-emulator-profile_mobile
%manifest %{name}.manifest
%config %{_sysconfdir}/config/emul_mobile.xml
%license LICENSE.Apache-2.0

%post -n model-config-emulator-profile_wearable
ln -sf emul_wearable.xml %{_sysconfdir}/config/model-config.xml
%files -n model-config-emulator-profile_wearable
%manifest %{name}.manifest
%config %{_sysconfdir}/config/emul_wearable.xml
%license LICENSE.Apache-2.0

%post -n model-config-emulator-profile_tv
ln -sf emul_tv.xml %{_sysconfdir}/config/model-config.xml
%files -n model-config-emulator-profile_tv
%manifest %{name}.manifest
%config %{_sysconfdir}/config/emul_tv.xml
%license LICENSE.Apache-2.0

%post -n model-config-generic
ln -sf generic.xml %{_sysconfdir}/config/model-config.xml
%files -n model-config-generic
%manifest %{name}.manifest
%config %{_sysconfdir}/config/generic.xml
%license LICENSE.Apache-2.0

%post -n model-config-default
ln -sf iot.xml %{_sysconfdir}/config/model-config.xml
%files -n model-config-default
%manifest %{name}.manifest
%config %{_sysconfdir}/config/iot.xml
%license LICENSE.Apache-2.0

%post -n model-config-tm1
ln -sf tm1.xml %{_sysconfdir}/config/model-config.xml
%files -n model-config-tm1
%manifest %{name}.manifest
%config %{_sysconfdir}/config/tm1.xml
%license LICENSE.Apache-2.0

%post -n model-config-n4
ln -sf tm2.xml %{_sysconfdir}/config/model-config.xml
%files -n model-config-n4
%manifest %{name}.manifest
%config %{_sysconfdir}/config/tm2.xml
%license LICENSE.Apache-2.0

%post -n model-config-tw2
ln -sf tw2.xml %{_sysconfdir}/config/model-config.xml
%files -n model-config-tw2
%manifest %{name}.manifest
%config %{_sysconfdir}/config/tw2.xml
%license LICENSE.Apache-2.0

%post -n model-config-xu3-profile_common
ln -sf xu3.xml %{_sysconfdir}/config/model-config.xml
%files -n model-config-xu3-profile_common
%manifest %{name}.manifest
%config %{_sysconfdir}/config/xu3.xml
%license LICENSE.Apache-2.0

%post -n model-config-xu3-profile_tv
ln -sf xu3_tv.xml %{_sysconfdir}/config/model-config.xml
%files -n model-config-xu3-profile_tv
%manifest %{name}.manifest
%config %{_sysconfdir}/config/xu3_tv.xml
%license LICENSE.Apache-2.0

%post -n model-config-rpi3-profile_common
ln -sf rpi3.xml %{_sysconfdir}/config/model-config.xml
%files -n model-config-rpi3-profile_common
%manifest %{name}.manifest
%config %{_sysconfdir}/config/rpi3.xml
%license LICENSE.Apache-2.0

%post -n model-config-rpi3-profile_tv
ln -sf rpi3_tv.xml %{_sysconfdir}/config/model-config.xml
%files -n model-config-rpi3-profile_tv
%manifest %{name}.manifest
%config %{_sysconfdir}/config/rpi3_tv.xml
%license LICENSE.Apache-2.0
