#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-modeldata
Version  : 0.1.1
Release  : 17
URL      : https://cran.r-project.org/src/contrib/modeldata_0.1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/modeldata_0.1.1.tar.gz
Summary  : Data Sets Used Useful for Modeling Packages
Group    : Development/Tools
License  : MIT
BuildRequires : buildreq-R

%description
packages are contained in this package.

%prep
%setup -q -c -n modeldata
cd %{_builddir}/modeldata

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1626371303

%install
export SOURCE_DATE_EPOCH=1626371303
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library modeldata
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library modeldata
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library modeldata
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc modeldata || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/modeldata/DESCRIPTION
/usr/lib64/R/library/modeldata/INDEX
/usr/lib64/R/library/modeldata/LICENSE
/usr/lib64/R/library/modeldata/Meta/Rd.rds
/usr/lib64/R/library/modeldata/Meta/data.rds
/usr/lib64/R/library/modeldata/Meta/features.rds
/usr/lib64/R/library/modeldata/Meta/hsearch.rds
/usr/lib64/R/library/modeldata/Meta/links.rds
/usr/lib64/R/library/modeldata/Meta/nsInfo.rds
/usr/lib64/R/library/modeldata/Meta/package.rds
/usr/lib64/R/library/modeldata/NAMESPACE
/usr/lib64/R/library/modeldata/NEWS.md
/usr/lib64/R/library/modeldata/R/modeldata
/usr/lib64/R/library/modeldata/R/modeldata.rdb
/usr/lib64/R/library/modeldata/R/modeldata.rdx
/usr/lib64/R/library/modeldata/data/Chicago.rda
/usr/lib64/R/library/modeldata/data/Sacramento.RData
/usr/lib64/R/library/modeldata/data/Smithsonian.RData
/usr/lib64/R/library/modeldata/data/ad_data.RData
/usr/lib64/R/library/modeldata/data/ames.rda
/usr/lib64/R/library/modeldata/data/attrition.RData
/usr/lib64/R/library/modeldata/data/biomass.RData
/usr/lib64/R/library/modeldata/data/bivariate.RData
/usr/lib64/R/library/modeldata/data/car_prices.RData
/usr/lib64/R/library/modeldata/data/cells.RData
/usr/lib64/R/library/modeldata/data/check_times.rda
/usr/lib64/R/library/modeldata/data/concrete.RData
/usr/lib64/R/library/modeldata/data/covers.RData
/usr/lib64/R/library/modeldata/data/credit_data.RData
/usr/lib64/R/library/modeldata/data/crickets.rda
/usr/lib64/R/library/modeldata/data/datalist
/usr/lib64/R/library/modeldata/data/drinks.rda
/usr/lib64/R/library/modeldata/data/grants.rda
/usr/lib64/R/library/modeldata/data/hpc_cv.rda
/usr/lib64/R/library/modeldata/data/hpc_data.RData
/usr/lib64/R/library/modeldata/data/lending_club.rda
/usr/lib64/R/library/modeldata/data/meats.RData
/usr/lib64/R/library/modeldata/data/mlc_churn.RData
/usr/lib64/R/library/modeldata/data/oils.RData
/usr/lib64/R/library/modeldata/data/okc.RData
/usr/lib64/R/library/modeldata/data/okc_text.rda
/usr/lib64/R/library/modeldata/data/parabolic.rda
/usr/lib64/R/library/modeldata/data/pathology.rda
/usr/lib64/R/library/modeldata/data/pd_speech.rda
/usr/lib64/R/library/modeldata/data/penguins.rda
/usr/lib64/R/library/modeldata/data/scat.RData
/usr/lib64/R/library/modeldata/data/small_fine_foods.RData
/usr/lib64/R/library/modeldata/data/solubility_test.rda
/usr/lib64/R/library/modeldata/data/stackoverflow.rda
/usr/lib64/R/library/modeldata/data/tate_text.rda
/usr/lib64/R/library/modeldata/data/two_class_dat.RData
/usr/lib64/R/library/modeldata/data/two_class_example.rda
/usr/lib64/R/library/modeldata/data/wa_churn.rda
/usr/lib64/R/library/modeldata/help/AnIndex
/usr/lib64/R/library/modeldata/help/aliases.rds
/usr/lib64/R/library/modeldata/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/modeldata/help/modeldata.rdb
/usr/lib64/R/library/modeldata/help/modeldata.rdx
/usr/lib64/R/library/modeldata/help/paths.rds
/usr/lib64/R/library/modeldata/html/00Index.html
/usr/lib64/R/library/modeldata/html/R.css
