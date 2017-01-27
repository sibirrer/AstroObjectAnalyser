


"""
Tests for `lenstronomy` module.
"""
from __future__ import print_function, division, absolute_import

import os

import pytest
from mock import patch
from darkskysync.DataSourceFactory import DataSourceFactory

from astroObjectAnalyser.strong_lens_data.data_manager import DataManager


class TestDataManager(object):

    @patch.object(DataSourceFactory, "fromConfig", autospec=False)
    def setup(self, dsf_object):
        #prepare unit test. Load data etc
        print("setting up " + __name__)
        test_dir = os.path.dirname(__file__ )
        sysdata_filepath = os.path.join(test_dir, 'Test_data', 'RXJ1131_1231.sysdata')
        self.fits_example = os.path.join(test_dir, 'Test_data', 'RXJ1131_1231_74010_cutout.fits')
        self.files = [sysdata_filepath, sysdata_filepath]
        self.datamanager = DataManager()

    def test_from_sysdata_files(self):
        data_list = self.datamanager._from_sysdata_files(self.files)
        assert len(data_list) == 2
        RXJ1131 = data_list[0]
        assert len(RXJ1131.data_cat) == 6
        assert len(RXJ1131.data_image) == 1

        assert RXJ1131.data_cat.name == 'RXJ1131-1231'
        assert RXJ1131.data_cat.ra_str == '11:31:51.4'
        assert RXJ1131.data_cat.dec_str == '-12:31:59'
        assert RXJ1131.data_cat.radius_est == '1.7'
        assert RXJ1131.data_cat.z_source == '0.658'
        assert RXJ1131.data_cat.z_lens == '0.295'
        assert RXJ1131.data_image.r_band == 'name_of_fits_file.fits'

    # def test_manage_fitsdata(self):
    #     local_file = self.datamanager.manage_fitsdata(self.fits_example)
    #
    #     assert os.path.isfile(local_file)
    #

    # def test_add_system_cental(self):
    #     pass
    #
    # def test_get_central_pickle(self):
    #     pass
    #
    # def test_from_clerk_table(self):
    #     pass
    #
    # def test_check_central_dir_access(self):
    #     pass
    #
    # def test_rd_pickle_file(self):
    #     pass
    #
    # def test_write_pickle_file(self):
    #     pass

    def test_get_data(self):

        data_list = self.datamanager.get_data(self.files,datatype='sysdata_file')
        data_list2 = self.datamanager._from_sysdata_files(self.files)
        assert data_list == data_list2

    def teardown(self):
        #tidy up
        print("tearing down " + __name__)
        pass

if __name__ == '__main__':
    pytest.main("-k TestDataManager")
