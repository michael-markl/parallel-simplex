import json

parTimesFile = open("par_times.json", encoding='utf-8')
parJson = json.loads(parTimesFile.read())
parTimesFile.close()

seqTimesFile = open("seq_times.json", encoding='utf-8')
seqJson = json.loads(seqTimesFile.read())
seqTimesFile.close()

output = ""

coordinates = ""
last_n = 0
for i in range(len(seqJson)):
    if seqJson[i]["n"] > last_n:
        coordinates += "(%i, %f)\n" % (seqJson[i]["n"], seqJson[i]["t"])
        last_n = seqJson[i]["n"]


output += r'''
\addplot coordinates { %% seq
    %s
};
''' % coordinates


for N in range(1, 5):
    last_n = 0
    coordinates = ""
    for i in range(len(parJson)):
        if parJson[i]["N"] == N and parJson[i]["n"] > last_n:
            coordinates += "(%i, %f)\n" % (parJson[i]["n"], parJson[i]["t"])
            last_n = parJson[i]["n"]
    output += r'''
        \addplot coordinates { %% %ix%i
            %s
        };
    ''' % (N, N, coordinates)

outputFile = open("times.tex", "w")
outputFile.write(output)
outputFile.close()