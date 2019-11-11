from database import *

CAUSE_GROUPS_1 = {
    # Infectious Disease
    'Infectous Intestinal Diseases': ('A00','A09'),
    'Tuberculosis': ('A15','A19'),
    'Zoonotic Bacterial Diseases': ('A20','A28'),
    'Other Bacterial Diseases': ('A30','A49'),
    'Sexually Transmitted Diseases': ('A50','A64'),
    'Syphilis, Yaws, Lyme, and other spirochetal': ('A65','A69'),
    'Other Chlamydiae diseases': ('A70','A74'),
    'Rickettsioses': ('A75', 'A79'),
    'Polio': 'A80',
    'Mad Cow Disaease, Kuru, and Fatal Familial Insomnia': 'A81',
    'Rabies': 'A82',
    'Encephalitis': ('A83','A86'),
    'Meningitis and other similar infections':('A87','A89'),
    'Mosquito Borne Illness': ('A90', 'A92'),
    'Viral and Hemorragic Fevers': ('A93','A99'),
    'Herpesviruses': ('B00', 'B10'),
    'Viral Hepatitus': ('B15', 'B20'),
    'HIV': 'B20',
    'Other Viral Diseases': ('B25', 'B34'),
    'Mycoses': ('B35','B49'),
    'Protozoal Diseases': ('B50', 'B64'),
    'Helminthiases': ('B65', 'B83'),
    'Pediculosis, Acariasis, and other Infestations': ('B85','B89'),
    'Sequelae of Infectious and Parasitic Diseases': ('B90','B94'),
    'Other Infectious diseases': ('B95','B99'),

    # Cancer
    'Oral Cancers': ('C00','C14'),
    'Upper GI Cancers': ('C15','C17'),
    'Colorectal Cancer': ('C18','C21'),
    'Liver, Gallbladder, and Pancreatic Cancers': ('C22','C26'),
    'Upper Respiratory Cancers': ('C30','C32'),
    'Lung Cancers': ('C33','C34'),
    'Bone Cancers': ('C40','C41'),
    'Skin Cancers': ('C43','C44'),
    'Soft Tissue Cancers': ('C45','C49'),
    'Breast Cancers': 'C50',
    'Female Genital Cancers': ('C51','C58'),
    'Male Genital Cancers': ('C60', 'C63'),
    'Urinary Tract Cancers': ('C64','C68'),
    'Nervous System Cancers': ('C69','C72'),
    'Thyroid and Endocrine Cancers': ('C73','C75'),
    'Endocrine Tumors': ('C7A','C7B'),
    'Cancers of Ill-Defined Sites': ('C76','C80'),
    'Blood Cancers and Lymphomas': ('C81','C96'),
    'Other Cancers and Benign Tumors': ('D00','D49'),

    # Blood based disease 
    'Nutritional Anemia': ('D50', 'D53'),
    'Hemolytic Anemia': ('D55','D59'),
    'Other anemia and bone marrow failure': ('D60','D64'),
    'Hemorrhagic Conditions': ('D65','D69'),
    'Other Blood Disorders': ('D70','D77'),
    'Surgical complications of the Spleen': 'D78',
    'Non-HIV Immunodeficiency': ('D80','D84'),
    'Sarcoidosis': 'D86',
    'Other Immune Disorders': 'D89',

    # Endocrine
    'Thyroid Disorders': ('E00', 'E07'),
    'Diabetes Mellitus': ('E08','E13'),
    'Other Endocrine Disorders': ('E15','E36'),
    'Nutritional deficiencies': ('E40','E64'),
    'Obesity': ('E65', 'E68'),
    'Metabolic Disorders': ('E70','E88'),
    'Surgical Complications of the Endocrine System': 'E89',

    # Mental
    'Mental Disorders due to Physiology': ('F01','F09'),
    'Mental Disorders due to Substance Abuse': ('F10','F19'),
    'Major Mental Illnesses, including Schizophrenia, Bipolar, etc': ('F20','F69'),
    'Intellectual Disabilities and other mental disorders': ('F70','F99'),

    # Nervous System
    'Inflammatory Disease of the CNS': ('G00','G09'),
    'Systematic CNS Atrophies': ('G10','G14'),
    'Extrapyramidal and Movement Disorders': ('G20','G26'),
    'Neurodegenerative Diseases': ('G30','G32'),
    'Misc Diseases of the CNS': ('G35','G99'),

    # Misc generally non-fatal
    'Disorders of the Eye':('H00','H59'),
    'Disorders of the ear': ('H60','H95'),
    'Disease of the Skin': ('L00','L99'),
    'Skeletal and Connective Tissue Diseases': ('M00','M99'),


    #Heart Disease
    'Rhumatic Heart Disease': ('I00','I09'),
    'Hypertensive Heart Disease': ('I10','I16'),
    'Ischemic Heart Disease': ('I20','I25'),
    'Other Heart Diseases': ('I26','I52'),
    'Stroke and Cerebrovascular Disease': ('I60','I69'),
    'Non Cardiopulmonary Circulatory Disease': ('I70','I99'),

    #Disgestive
    'Oral Disease': ('K00','K14'),
    'Upper GI Disease': ('K20','K31'),
    'Disease of the Appendix': ('K35','K38'),
    'Hernias': ('K40','K46'),
    'Lower GI Disease': ('K50','K64'),
    'Disease of the Peritoneum': ('K65','K68'),
    'Liver Disease': ('K70','K77'),
    'Gallbladder and Pancreatic Disease': ('K80', 'K87'),
    'Other Digestive Disease': ('K90','K95'),



}

CAUSE_GROUPS_2 = {
    'Infectious Disease': [('A00','B99'),(1001,1025)],
    'Cancer': [('C00','D49'),(1026,1047)],
    'Blood Diseases': [('D50','D89'),(1048,1050)],
    'Diabetes and Endocrine Disorders': [('E00','E89'),(1051,1054)],
    'Mental Illness': [('F01','F99'),(1055,1057)],
    'Central Nervous System Disease': [('G00','G99'),(1058,1061)],
    'Disease of the Eye or Ear': [('H00','H95'),(1062,1063)],
    'Disaese of the Skin': [('L00','L99'),(1082)],
    'Musculoskeletal and Connective Tissue Disease': [('M00','M99'),(1083)],
    'Heart Disease': [('I00','I99'),(1064,1071)],
    'Respiratory Disease': [('J00','J98'),(1072,1077)],
    'Digestive Disease': [('K00','K95'),(1078,1081)],
    'Kidney Disease': [('N00','N39'),(1084,1085)],
    'Diseases of the Sexual Organs and Breasts': [('N40','N99'),(1086)],
    'Complications of Pregnancy': [('O00','O9A'),(1087,1091)],
    'Congenial Disorders': [('P00','Q99'),(1093)],
    'External Causes': [('V01','X09'),(1095,1096)],
    'Accidental Poisoning': [('X40','X49'),(1100)],
    'Suicide': [('X60','X84'),(1101)],
    'Assault': [('X85','Y09'),(1102)]
    

}

def query_deaths(country, sex, year, cause_str):

    if sex == 1:
        pass

    cause = CAUSE_GROUPS_2[cause_str]
    
    query_1 = '''
            SELECT * FROM who_mortality WHERE 
                country='{}' AND
                sex='{}' AND
                year='{}' AND
                cause>'{}' AND 
                cause<'{}';
            '''
    query_2 = '''
            SELECT * FROM who_mortality WHERE 
                country='{}' AND
                sex='{}' AND
                year='{}' AND
                cause='{}';
            '''

    db = Database()
    rows = []

    for interval in cause:
        if type(interval) == tuple and len(interval) == 2:
            query = query_1.format(
                country,
                sex,
                year,
                numerical_encode_cause(interval[0])-1,
                numerical_encode_cause(interval[1])+1
            )
        else:
            query = query_2.format(
                country,
                sex,
                year,
                numerical_encode_cause(interval)
            )
        
        res = db.raw_query(query)
        for r in res:
            rows.append(r)
    
    #Sum up results from index 6 to the end

    result = [0]*26

    for row in rows:
        for index in range(len(row)):
            if index > 5:
                result[index-6] += row[index]

    return result

print(query_deaths(2090,1,2015,'Cancer'))
print(query_deaths(2090,2,2015,'Cancer'))
print(query_deaths(2090,1,2015,'Suicide'))
print(query_deaths(2090,2,2015,'Suicide'))
