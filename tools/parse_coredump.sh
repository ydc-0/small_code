export IDF_PATH=~/esp32/esp-idf


for dumpfile in ./*.bin
do
    echo $dumpfile
    python $IDF_PATH/components/espcoredump/espcoredump.py info_corefile -t b64 -c $dumpfile ssc.elf > ./core_info/$dumpfile.txt
done
