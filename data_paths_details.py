import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='Get stats and clean csv')
parser.add_argument('--tsvfile', '-tf',
                        help='Input the path for the tsv file')

parser.add_argument('--savecsv','-sc', help = 'True for saving final csv, False for not')

args = parser.parse_args()
input_file=args.tsvfile
save_csv=args.savecsv


dataset = pd.read_csv(input_file,sep="\t")
language = dataset["locale"][0]
if language == "en":
    dataset2 = dataset[(dataset["age"].isna()==False) & (dataset["gender"].isna()==False) & (dataset["accent"].isna()==False) & (dataset["sentence"].isna()==False)]
else:
     dataset2 = dataset[(dataset["age"].isna()==False) & (dataset["gender"].isna()==False) & (dataset["sentence"].isna()==False)]

#language = dataset["locale"][0]

output = pd.DataFrame()
output["wav_path"] = '/media/data_dump/hemant/common_voice_Data/' + language + '/wav/' + dataset2["path"]
output["transcript_path"] = '/media/data_dump/hemant/common_voice_Data/' + language + '/text/' + dataset2["path"].str[:-3] + 'txt'

output["age"] = dataset2["age"]
output["gender"] = dataset2["gender"]
output["accent"] = dataset2["accent"]

if save_csv:
    output.to_csv(input_file.split("/")[-1][:-4] + language + ".csv",index= False)

print("--------------------Showing Accent Statisctics--------------------")
print(output['accent'].value_counts())
print("--------------------Showing Gender Statistics--------------------")
print(output['gender'].value_counts())
print("--------------------Showing Age Statistics--------------------")
print(output['age'].value_counts())
percentage = (dataset2.shape[0]/dataset.shape[0])*100
print("Showing Stats for " +str( percentage) + "% of rows")

#output['accent'].value_counts().reset_index().to_csv("accent" + "_" + input_file.split("/")[-1][:-4] + "_" + language + ".txt")
#output['age'].value_counts().reset_index().to_csv("age" + "_" + input_file.split("/")[-1][:-4] + "_" + language + ".txt")
#output['gender'].value_counts().reset_index().to_csv("gender" + "_" + input_file.split("/")[-1][:-4] + "_" + language + ".txt")
