from pages.social_media_links_page import SocialMediaLinksPage


def test_twitter_link(login):
    social_media_links_page = SocialMediaLinksPage(login)
    social_media_links_page.verify_twitter_link()


def test_facebook_link(login):
    social_media_links_page = SocialMediaLinksPage(login)
    social_media_links_page.verify_facebook_link()


def test_linkedin_link(login):
    social_media_links_page = SocialMediaLinksPage(login)
    social_media_links_page.verify_linkedin_link()



