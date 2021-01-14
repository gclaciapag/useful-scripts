import matplotlib as plt
import sys
import csv


def open_spectrum_file(filename):
    file_array = []
    with open(filename) as f:
        for line in f:
            file_array.append(line.split("\t"))
    return file_array


def open_tpc_wavenum_file(filename):
    tpc_wavenum_array = []
    with open(filename) as f:
        for line in f:
            tpc_wavenum_array.append(float(line))
    return tpc_wavenum_array


def get_spectrum(spectrum_file):
    wave = []
    trans = []
    for line in spectrum_file:
        if line[0] not in wave:
            wave.append(line[0])
            trans.append(line[1])
    wavenumber = [float(w[:4]) * 10**int(w[-1]) for w in wave[1:]]
    transmittance = [float(t[:4]) * 10**int(t[-2]) for t in trans[1:]]
    return wavenumber, transmittance


def convert_to_tpc_format(sonion_wave, tpc_wave, sonion_trans):
    sonion_wave_trans = {}
    for i in range(len(sonion_wave)):
        sonion_wave_trans[sonion_wave[i]] = sonion_trans[i]

    tpc_wave_trans = []
    for i in range(len(tpc_wave)):
        found = False
        for item in sonion_wave_trans:
            if int(tpc_wave[i]) == int(item):
                tpc_wave_trans.append(sonion_wave_trans[item])
                found = True
                break
            elif abs(int(tpc_wave[i]) - int(item)) <= 10:
                tpc_wave_trans.append(sonion_wave_trans[item])
                found = True
                break

        if not found:
            tpc_wave_trans.append(tpc_wave_trans[-1])

    return tpc_wave_trans


def save_file(file_title, wavenum, trans):
    with open(file_title, "w") as f:
        for i in range(len(wavenum)):
            f.write(f"{wavenum[i]} {trans[i]}\n")


sonion_ = sys.argv[1]
tpc_ = sys.argv[2]
converted_file_name = sys.argv[3]

sonion_file = open_spectrum_file(sonion_)
tpc_wavenum = open_tpc_wavenum_file(tpc_)
sonion_wavenum, sonion_trans = get_spectrum(sonion_file)
tpc_trans = convert_to_tpc_format(sonion_wavenum, tpc_wavenum, sonion_trans)
save_file(converted_file_name, tpc_wavenum, tpc_trans)
