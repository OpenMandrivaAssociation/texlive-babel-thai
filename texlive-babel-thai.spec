# revision 30564
# category Package
# catalog-ctan /macros/latex/contrib/babel-contrib/thai
# catalog-date 2013-05-19 01:05:23 +0200
# catalog-license lppl1.3
# catalog-version 1.0.0
Name:		texlive-babel-thai
Version:	1.0.0
Release:	8
Summary:	Support for Thai within babel
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/thai
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-thai.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-thai.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-thai.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides support for typesetting Thai text. within
the babel system.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-thai/lthenc.def
%{_texmfdistdir}/tex/generic/babel-thai/thai.ldf
%{_texmfdistdir}/tex/generic/babel-thai/tis620.def
%doc %{_texmfdistdir}/doc/generic/babel-thai/thai.pdf
#- source
%doc %{_texmfdistdir}/source/generic/babel-thai/thai.dtx
%doc %{_texmfdistdir}/source/generic/babel-thai/thai.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
