def load_profile(file_path):
    linkedin_profile = ''
    with open(file_path,'r',encoding='utf-8') as f:
        for line in f.readlines():
            linkedin_profile = linkedin_profile + line
    return linkedin_profile




