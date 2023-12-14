from tests import Tests


def test_required():
    Tests.test0_test_site_site_passkey_class_constructor()
    Tests.test1_test_site_passkey_class_setters()
    Tests.test2_test_passphrase_generator_class_read_file()
    Tests.test3_test_passphrase_generator_class_generate_passphrase_default_length()
    Tests.test4_test_passphrase_generator_class_generate_passphrase_custom_length()
    Tests.test5_test_site_passphrase_manager_class_add()
    Tests.test6_test_site_passphrase_manager_class_getters()
    Tests.test7_test_site_passphrase_manager_class_refresh_password()
    Tests.test8_test_site_passphrase_manager_class_save_to_file()
    Tests.test9_test_site_passphrase_manager_class_load_from_file()

def main():
    test_required()

if __name__ == '__main__':
    main()