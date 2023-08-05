import json
import logging

from pathlib import Path


log = logging.getLogger(__name__)

rat_template = '''
{
  "names": {
    "reddit": [],
    "redgifs": [],
    "onlyfans": [],
    "fansly": [],
    "pornhub": [],
    "twitter": [],
    "instagram": [],
    "youtube": [],
    "tiktok": [],
    "twitch": [],
    "patreon": [],
    "tumblr": [],
    "myfreecams": [],
    "chaturbate": []
  },
  "links": {
    "coomer": [],
    "simpcity": []
  },
  "urls_to_download": [],
  "urls_downloaded": [],
  "file_hashes": {},
  "error_dictionaries": []
}
'''


def get_rat_name():
    log.debug("Returning .rat name")
    return Path.cwd().stem + '.rat'


def get_rat_template():
    log.debug("Returning copy of rat template")
    return json.loads(rat_template)


def write_rat_file(template):
    log.debug("Writing rat file")
    rat_name = get_rat_name()
    with open(f"{rat_name}", 'w') as f:
        json.dump(template, f, indent=2)


def rat_file_exists():
    log.debug("Checking if .rat file exists")
    files = list(Path.cwd().glob("*.rat"))

    if len(files) > 1:
        log.info("Too many .rat files")
        return False

    elif len(files) == 0:
        # rat_name = get_rat_name()
        # template = json.loads(rat_template)
        log.info("Missing .rat file")
        return False
    elif len(files) == 1:
        return True


def get_rat_info():
    log.debug("Returning stored information from the .rat")

    if rat_file_exists():
        rat_name = get_rat_name()
        with open(f'{rat_name}', 'r') as f:
            rat_contents = json.load(f)
        return rat_contents
    else:
        return 'missing'


def check_existence(category_1, entry):

    rat_contents = get_rat_info()
    if rat_contents == 'too_many' or rat_contents == 'missing':
        pass

    else:

        if category_1 == 'urls_downloaded':
            if entry in rat_contents['urls_downloaded']:
                return True
            else:
                return False


def add_entry(**kwargs):
    if kwargs:
        if kwargs['category_1']:
            category_1 = kwargs['category_1']

        if kwargs['entry']:
            entry = str(kwargs['entry'])

    rat_contents = get_rat_info()
    if rat_contents == 'too_many' or rat_contents == 'missing':
        pass

    else:

        if category_1 == 'urls_downloaded':
            stored_urls = rat_contents['urls_downloaded']
            stored_urls.append(entry)
            rat_contents['urls_downloaded'] = sorted(list(set(stored_urls)))

        rat_name = get_rat_name()
        with open(f"{rat_name}", 'w') as f:
            json.dump(rat_contents, f, indent=2)


def print_rat(category_1, category_2=None, respond=False):

    rat_contents = get_rat_info()

    if rat_contents == 'too_many':
        print("Too many .rat files found")

    elif rat_contents == 'missing':
        print("No .rat file found")

    else:
        try:
            if category_1 == 'names':

                entries: list[str] = []

                for x in rat_contents['names'][category_2]:
                    entries.append(x)

                if respond is True:
                    return entries

                else:
                    print(*entries, sep='\n')

            if category_1 == 'links':
                for x in rat_contents['links'][category_2]:
                    print(x)

            elif category_1 == 'urls_to_download':
                for x in rat_contents['urls_to_download']:
                    print(x)

            elif category_1 == 'urls_downloaded':
                for x in rat_contents['urls_downloaded']:
                    print(x)

            elif category_1 == 'errors':
                for x in rat_contents['error_dictionaries']:
                    print(x)

        except KeyError:
            print("No Entry Found")


def synced_rat_template():

    log.debug("Syncing the current .rat info with the current template")
    rat_contents = get_rat_info()

    if rat_contents == 'too_many':
        log.warn("Too many .rat files found")
        return

    elif rat_contents == 'missing':

        template = get_rat_template()
        return template

    else:

        template = get_rat_template()
        for name in rat_contents['names']:
            if name == 'reddit':
                for y in rat_contents['names']['reddit']:
                    template['names']['reddit'].append(y)

            if name == 'redgifs':
                for y in rat_contents['names']['redgifs']:
                    template['names']['redgifs'].append(y)

            if name == 'onlyfans':
                for y in rat_contents['names']['onlyfans']:
                    template['names']['onlyfans'].append(y)

            if name == 'fansly':
                for y in rat_contents['names']['fansly']:
                    template['names']['fansly'].append(y)

            if name == 'pornhub':
                for y in rat_contents['names']['pornhub']:
                    template['names']['pornhub'].append(y)

            if name == 'twitter':
                for y in rat_contents['names']['twitter']:
                    template['names']['twitter'].append(y)

            if name == 'instagram':
                for y in rat_contents['names']['instagram']:
                    template['names']['instagram'].append(y)

            if name == 'youtube':
                for y in rat_contents['names']['youtube']:
                    template['names']['youtube'].append(y)

            if name == 'tiktok':
                for y in rat_contents['names']['tiktok']:
                    template['names']['tiktok'].append(y)

            if name == 'twitch':
                for y in rat_contents['names']['twitch']:
                    template['names']['twitch'].append(y)

            if name == 'patreon':
                for y in rat_contents['names']['patreon']:
                    template['names']['patreon'].append(y)

            if name == 'tumblr':
                for y in rat_contents['names']['tumblr']:
                    template['names']['tumblr'].append(y)

            if name == 'myfreecams':
                for y in rat_contents['names']['myfreecams']:
                    template['names']['myfreecams'].append(y)

            if name == 'chaturbate':
                for y in rat_contents['names']['chaturbate']:
                    template['names']['chaturbate'].append(y)

        for link in rat_contents['links']:

            if link == 'coomer':
                for link in rat_contents['links']['coomer']:
                    template['links']['coomer'].append(link)

            if link == 'simpcity':
                for link in rat_contents['links']['simpcity']:
                    template['links']['simpcity'].append(link)

        for url in rat_contents['urls_to_download']:
            template['urls_to_download'].append(url)

        for url in rat_contents['urls_downloaded']:
            template['urls_downloaded'].append(url)

        if rat_contents.get('file_hashes'):
            template['file_hashes'] = rat_contents['file_hashes']

        else:
            template['file_hashes'] = {}

        if rat_contents.get('error_dictionaries'):
            template['error_dictionaries'] = rat_contents['error_dictionaries']

        else:
            template['error_dictionaries'] = []

        return template


def update_rat(category_1, category_2=None, category_3=None):

    log.debug("Updating the .rat with new info")
    template = synced_rat_template()

    if category_1 == 'names':
        x = template['names'][category_2]
        x.append(category_3.strip())
        template['names'][category_2] = sorted(list(set(x)))

    if category_1 == 'links':
        x = template['links'][category_2]
        x.append(category_3.strip())
        template['links'][category_2] = sorted(list(set(x)))

    if category_1 == 'urls_to_download':
        x = template['urls_to_download']
        x.append(category_3.strip())
        template['urls_to_download'] = sorted(list(set(x)))

    if category_1 == 'urls_downloaded':
        x = template['urls_downloaded']
        x.append(category_3.strip())
        template['urls_downloaded'] = sorted(list(set(x)))

    if category_1 == 'file_hashes':
        template['file_hashes'] = category_2

    write_rat_file(template)


def get_file_hashes() -> dict[str, str]:

    if rat_file_exists():
        template = synced_rat_template()
        return template['file_hashes']

    else:
        return


def get_urls_to_download() -> list[str] | list:

    if rat_file_exists():
        template = synced_rat_template()
        return template['urls_to_download']

    else:
        return []


def get_downloaded_urls() -> list[str] | list:

    if rat_file_exists():
        template = synced_rat_template()
        return template['urls_downloaded']

    else:
        return []


def add_error_dictionary(url_dictionary):

    template = synced_rat_template()

    if url_dictionary.get('response'):
        del url_dictionary['response']

    error_dictionaries = template['error_dictionaries']
    if len(error_dictionaries) == 0:
        url_dictionary['retries'] = 1
        template['error_dictionaries'] = []
        template['error_dictionaries'].append(url_dictionary)
        write_rat_file(template)

    else:
        already_stored = False
        try:
            for index, error_dictionary in enumerate(template['error_dictionaries']):
                for key, value in error_dictionary.items():
                    if key == 'url' and value == url_dictionary['url']:
                        already_stored = True
                        count = error_dictionary['retries']
                        count += 1
                        log.debug(
                            f"url_dictionary has already been stored. Increasing error attempt count to {count}")
                        if count > 5:
                            log.warn(
                                f"Already attempted 5 times. Removing from being attempted again. {url_dictionary['url_to_download']}")
                            del template['error_dictionaries'][index]
                        else:
                            template['error_dictionaries'][index]['retries'] = count
        except KeyError:
            pass

        if already_stored is False:
            log.debug(
                f"url_dictionary has not had an error yet. Storing it for later")
            url_dictionary['retries'] = 1
            template['error_dictionaries'].append(url_dictionary)

        write_rat_file(template)


def remove_error_dictionary(url_dictionary):

    template = synced_rat_template()

    for index, error_url_dictionary in enumerate(template['error_dictionaries']):
        for key, value in error_url_dictionary:
            if key == 'urls_to_download' and value == url_dictionary['urls_to_download']:
                del template['error_dictionaries'][index]

    write_rat_file(template)


def get_error_dictionaries():

    template = synced_rat_template()

    return template['error_dictionaries']


def erase_error_dictionaries():

    log.debug("Erasing error dictionaries")

    template = synced_rat_template()

    template['error_dictionaries'] = []

    write_rat_file(template)
