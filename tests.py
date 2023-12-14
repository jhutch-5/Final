import random
from passphrase_generator import PassphraseGenerator
from site_passphrase import SitePassphrase
from site_passphrase_manager import SitePassphraseManager

class Tests:
    def test0_test_site_site_passkey_class_constructor():
        site_passkey = SitePassphrase('Amazon', 'www.amazon.com', 'waffles@cheetos.com', 'cleft cam synod lacy yr wok')

        assert site_passkey.get_site_name() == 'Amazon'
        assert site_passkey.get_site_url() == 'www.amazon.com'
        assert site_passkey.get_username() == 'waffles@cheetos.com'
        assert site_passkey.get_passphrase() == 'cleft cam synod lacy yr wok'

        print('TEST0: PASSED')
    def test1_test_site_passkey_class_setters():
        site_passkey = SitePassphrase('Amazon', 'www.amazon.com', 'waffles@cheetos.com', 'cleft cam synod lacy yr wok')
        site_passkey.set_site_name('Google')
        site_passkey.set_site_url('www.google.com')
        site_passkey.set_username('waffles2@cheetos.com')
        site_passkey.set_passphrase('synod cam lacy yr wok cleft')

        assert site_passkey.get_site_name() == 'Google'
        assert site_passkey.get_site_url() == 'www.google.com'
        assert site_passkey.get_username() == 'waffles2@cheetos.com'
        assert site_passkey.get_passphrase() == 'synod cam lacy yr wok cleft'


        print('TEST1: PASSED')
    
    def test2_test_passphrase_generator_class_read_file():

        passphrase_generator = PassphraseGenerator(random.Random(0))
        assert passphrase_generator.get_words_count() == 7776

        print('TEST2: PASSED')
    
    def test3_test_passphrase_generator_class_generate_passphrase_default_length():
        passphrase_generator = PassphraseGenerator(random.Random(0))
        
        passphrase = passphrase_generator.generate()

        assert len(passphrase.split(' ')) == 5

        print('TEST3: PASSED')

    def test4_test_passphrase_generator_class_generate_passphrase_custom_length():
        passphrase_generator = PassphraseGenerator(random.Random(0))
        
        passphrase = passphrase_generator.generate(10)

        assert len(passphrase.split(' ')) == 10

        print('TEST4: PASSED')
    
    def test5_test_site_passphrase_manager_class_add():
        site_passphrase_manager = SitePassphraseManager(PassphraseGenerator(random.Random(0)), random.Random(0))
        site_passphrase_manager.add('Amazon', 'www.amazon.com', 'waffles@cheetos.com')

        assert site_passphrase_manager.get_count() == 1

        print('TEST5: PASSED')

    def test6_test_site_passphrase_manager_class_getters():
        site_passkey_manager = SitePassphraseManager(PassphraseGenerator(random.Random(0)), random.Random(0))
        site_passkey_manager.add('Amazon', 'www.amazon.com', 'waffles@cheetos.com', 'cleft cam synod lacy yr wok')

        assert site_passkey_manager.get_passphrase_for_site('Amazon') == 'cleft cam synod lacy yr wok'

        print('TEST6: PASSED')

    
    def test7_test_site_passphrase_manager_class_refresh_password():
        site_passkey_manager = SitePassphraseManager(PassphraseGenerator(random.Random(0)), random.Random(0))
        site_passkey_manager.add('Amazon', 'www.amazon.com', 'waffles@cheetos.com', 'cleft cam synod lacy yr wok')

        site_passkey_manager.refresh_password_for_site('Amazon')

        assert site_passkey_manager.get_passphrase_for_site('Amazon') != 'cleft cam synod lacy yr wok'
                                 
        print('TEST7: PASSED')

    def test8_test_site_passphrase_manager_class_save_to_file():
        site_passkey_manager = SitePassphraseManager(PassphraseGenerator(random.Random(0)), random.Random(0))
        
        site_passkey_manager.add('Amazon', 'www.amazon.com', 'waffles@cheetos.com', 'cleft cam synod lacy yr wok')
        site_passkey_manager.add('Google', 'www.google.com', 'waffles@cheetos.com', 'cleft cam synod lacy yr wok')
        site_passkey_manager.add('Facebook', 'www.facebook.com', 'waffles@cheetos.com', 'cleft cam synod lacy yr wok')
        
        site_passkey_manager.save('test_file.txt')

        site_passkey_manager = SitePassphraseManager(PassphraseGenerator(random.Random(0)), random.Random(0), 'test_file.txt')

        assert site_passkey_manager.get_count() == 3

        amazon_passphrase = site_passkey_manager.get_passphrase_for_site('Amazon')
        google_passphrase = site_passkey_manager.get_passphrase_for_site('Google')
        facebook_passphrase = site_passkey_manager.get_passphrase_for_site('Facebook')

        assert amazon_passphrase == 'cleft cam synod lacy yr wok'
        assert google_passphrase == 'cleft cam synod lacy yr wok'
        assert facebook_passphrase == 'cleft cam synod lacy yr wok'
        
        print('TEST8: PASSED')

    def test9_test_site_passphrase_manager_class_load_from_file():
        site_passkey_manager = SitePassphraseManager(PassphraseGenerator(random.Random(0)), random.Random(0), 'passphrases.txt')
        
        assert site_passkey_manager.get_count() == 3

        amazon_passphrase = site_passkey_manager.get_passphrase_for_site('Amazon')
        google_passphrase = site_passkey_manager.get_passphrase_for_site('Google')
        facebook_passphrase = site_passkey_manager.get_passphrase_for_site('Facebook')
        
        assert amazon_passphrase == 'cleft cam synod lacy yr wok'
        assert google_passphrase == 'cleft cam synod lacy yr wok'
        assert facebook_passphrase == 'cleft cam synod lacy yr wok'

        print('TEST9: PASSED')

        