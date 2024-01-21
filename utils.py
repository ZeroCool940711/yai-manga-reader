import os
from whoosh import index
from config.db.Model import Options

if not os.path.exists("db"):
    os.mkdir("db")
    
def first_run():
    if not check_if_index_exists("db",'options'):
        set_default_config()
        return True
    else:
        return False
    
def create_index(schema, indexname):
    # Using the convenience functions
    ix = index.create_in("db", schema=schema, indexname=indexname)
    return ix

def open_index(dirname, indexname, schema):
    # Using the convenience functions
    ix = index.open_dir(dirname=dirname, indexname=indexname, schema=schema)
    return ix
    
def check_if_index_exists(dirname, indexname):
    return index.exists_in(dirname, indexname=indexname)
    
def set_default_config(reset=False):
    """
    Set default config for the app. We will use this to create the index for the first time.
    The idea is to store and access the options incrementally while keeping previous versions
    as previous/older documents in the index in case we want to revert to a previous version.
    If we want to reset everything to default, we can just delete the index and create a new one with the defaults.
    """
    defaults = {
        "app_title": "Yai Manga Reader",
        "theme_mode": "dark",
        "language": "en",
        "show_nav_bar_updates": False,
        "show_nav_bar_history": False,
        "show_nav_bar_labels": True,
        "expand_search_filters": False,
        "recommendations_in_overflow_menu": False,
        "merge_in_overflow_menu": True,
        "per_category_sorting": True,
        "automatic_updates_interval": 12,
        "automatically_refresh_metadata": True,
        "show_unread_count_in_update_button": False,
    }
    if reset:
        ix = create_index(Options, "options")
        
    if check_if_index_exists("db", "options"):        
        ix = index.open_dir("db", indexname="options", schema=Options)
    else:
        ix = create_index(Options, "options")
        
    writer = ix.writer()
    writer.add_document(**defaults)
    writer.commit(merge=True, optimize=True)
    
def get_options(dirname="db", indexname="options", last_version=True):
    ix = open_index(dirname, indexname, schema=Options)
    with ix.searcher() as searcher:
        results = searcher.documents()
        #for result in results:
        #    print (result)
        if last_version:
            # return last version only
            for result in results:
                return result
        else:
            # return all versions
            return list(results)
        
#defaults = set_default_config()
#print (first_run())
#print (get_options(last_version=True))
#print(check_if_index_exists("db", "options"))