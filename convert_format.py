import math
import matplotlib.pyplot as plt
import sys


def create_array_from_file(filename):
    array = []
    with open(filename) as f:
        for line in f:
            array.append(float(line))
    return array


def plot_spectra(filename):
    figure, (plt1, plt2) = plt.subplots(1, 2)

    plt1.plot(x1[:423], y1[:423])
    plt1.invert_xaxis()
    plt1.set_title("Sonion")

    plt2.plot(x2, y2[:423])
    plt2.invert_xaxis()
    plt2.set_title("TPC")

    figure.tight_layout()
    # plt.show()
    plt.savefig(filename)


def convert_to_transmittance(absorbance):
    transmittance = [(math.exp((i * -1)) * 100) for i in absorbance]
    return transmittance


def convert_transmittance_to_tpc_format(sonion_wav, tpc_wav, trans):
    sonion_wav_abs = {}

    for i in range(423):
        sonion_wav_abs[sonion_wav[i]] = abs_[i]

    tpc_wav_abs = []
    for i in range(len(tpc_wav)):
        found = False
        for item in sonion_wav_abs:
            if int(tpc_wav[i] == int(item)):
                tpc_wav_abs.append(sonion_wav_abs[item])
                found = True
                break
            elif abs(int(tpc_wav[i]) - int(item)) <= 10:
                tpc_wav_abs.append(sonion_wav_abs[item])
                found = True
                break

        if not found:
            tpc_wav_abs.append(tpc_wav_abs[-1])

    return convert_to_transmittance(tpc_wav_abs)


file1 = sys.argv[1]
file2 = sys.argv[2]
file3 = sys.argv[3]
file4 = sys.argv[4]

tpc_wav = create_array_from_file(file1)
sonion_wav = create_array_from_file(file2)
abs_ = create_array_from_file(file3)
trans_ = create_array_from_file(file4)

# Before transformation
x1 = sonion_wav
x2 = tpc_wav
y1 = trans_
y2 = y1

plot_spectra("Before Transformation")


# After transformation
y2 = convert_transmittance_to_tpc_format(sonion_wav, tpc_wav, trans_)

plot_spectra("After Transformation")
