#!/usr/bin/python

from base import WebTest, USER, PASS
from runner import test_runner

class PageTests(WebTest):

    def __init__(self):
        WebTest.__init__(self)
        self.login(USER, PASS)
        self.rest()

    def search(self):
        list_item = self.by_class('menu_search')
        list_item.find_element_by_tag_name('a').click()
        self.rest()
        assert self.by_class('content_title').text[0:6] == 'Search'

    def sent(self):
        list_item = self.by_class('menu_sent')
        list_item.find_element_by_tag_name('a').click()
        self.rest()
        assert self.by_class('mailbox_list_title').text == 'Sent'

    def unread(self):
        list_item = self.by_class('menu_unread')
        list_item.find_element_by_tag_name('a').click()
        self.rest()
        assert self.by_class('mailbox_list_title').text == 'Unread'

    def combined_inbox(self):
        list_item = self.by_class('menu_combined_inbox')
        list_item.find_element_by_tag_name('a').click()
        self.rest()
        assert self.by_class('mailbox_list_title').text == 'Everything'

    def flagged(self):
        list_item = self.by_class('menu_flagged')
        list_item.find_element_by_tag_name('a').click()
        self.rest()
        assert self.by_class('mailbox_list_title').text == 'Flagged'

    def contacts(self):
        if not self.mod_active('contacts'):
            return
        list_item = self.by_class('menu_contacts')
        list_item.find_element_by_tag_name('a').click()
        self.rest()
        assert self.by_class('content_title').text == 'Contacts'

    def compose(self):
        list_item = self.by_class('menu_compose')
        list_item.find_element_by_tag_name('a').click()
        self.rest()
        assert self.by_class('content_title').text == 'Compose'

    def calendar(self):
        if not self.mod_active('smtp'):
            return
        list_item = self.by_class('menu_calendar')
        list_item.find_element_by_tag_name('a').click()
        self.rest()
        assert self.by_class('content_title').text == 'Calendar'

    def history(self):
        if not self.mod_active('history'):
            return
        list_item = self.by_class('menu_history')
        list_item.find_element_by_tag_name('a').click()
        self.rest()
        assert self.by_class('content_title').text == 'Message history'

    def home(self):
        self.by_css('[data-source=".settings"]').click()
        list_item = self.by_class('menu_home')
        list_item.find_element_by_tag_name('a').click()
        self.rest()
        assert self.by_class('content_title').text == 'Home'

    def servers(self):
        list_item = self.by_class('menu_servers')
        list_item.find_element_by_tag_name('a').click()
        self.rest()
        assert self.by_class('content_title').text == 'Servers'

    def site(self):
        list_item = self.by_class('menu_settings')
        list_item.find_element_by_tag_name('a').click()
        self.rest()
        assert self.by_class('content_title').text == 'Site Settings'

    def save(self):
        list_item = self.by_class('menu_save')
        list_item.find_element_by_tag_name('a').click()
        self.rest()
        assert self.by_class('content_title').text == 'Save Settings'

    def password(self):
        try:
            list_item = self.by_class('menu_change_password')
            list_item.find_element_by_tag_name('a').click()
            self.rest()
            assert self.by_class('content_title').text == 'Change Password'
        except AttributeError:
            pass

    def profiles(self):
        if self.mod_active('profiles'):
            return
        list_item = self.by_class('menu_profiles')
        list_item.find_element_by_tag_name('a').click()
        self.rest()
        assert self.by_class('content_title').text == 'Profiles'

if __name__ == '__main__':

    print "PAGE TESTS"
    test_runner(PageTests, [
        'search',
        'combined_inbox',
        'unread',
        'sent',
        'flagged',
        'contacts',
        'compose',
        'calendar',
        'history',
        'home',
        'servers',
        'site',
        'save',
        'password',
        'profiles',
        'logout',
    ])
