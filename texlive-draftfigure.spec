Name:		texlive-draftfigure
Version:	44854
Release:	2
Summary:	Replace figures with a white box and additional features
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/draftfigure
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/draftfigure.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/draftfigure.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
With this package you can control the outcome of a figure which
is set to draft and modify the display with various options.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/draftfigure
%doc %{_texmfdistdir}/doc/latex/draftfigure

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
