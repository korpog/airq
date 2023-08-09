import matplotlib.pyplot as plt
import pandas as pd

plt.style.use("Solarize_Light2")

df = pd.read_csv("csv/wokalna_clean.csv", index_col=0,
                 parse_dates=['utc', 'local'])

no2 = df[df["parameter"] == "no2"]
o3 = df[df["parameter"] == "o3"]
pm25 = df[df["parameter"] == "pm25"]

# group by an hour of the day and get mean value for every hour
no2_hour = no2.groupby(no2["local"].dt.hour).agg(hourly_avg=('value', 'mean'))
o3_hour = o3.groupby(o3["local"].dt.hour).agg(hourly_avg=('value', 'mean'))
pm25_hour = pm25.groupby(pm25["local"].dt.hour).agg(
    hourly_avg=('value', 'mean'))

# group by the day and get mean value and standard deviation for every day in the month
no2_day = no2.groupby(no2["local"].dt.day).agg(
    daily=('value', 'mean'), std=('value', 'std'),
    min=('value', 'min'), max=('value', 'max'))
o3_day = o3.groupby(o3["local"].dt.day).agg(
    daily=('value', 'mean'), std=('value', 'std'),
    min=('value', 'min'), max=('value', 'max'))
pm25_day = pm25.groupby(pm25["local"].dt.day).agg(
    daily=('value', 'mean'), std=('value', 'std'),
    min=('value', 'min'), max=('value', 'max'))


def daily_minmax():
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, sharex='col', layout='constrained')
    fig.set_figwidth(20)
    fig.supxlabel("Day")
    fig.supylabel("[µg/m³]")

    ax1.set_title(r'$NO_2$')
    ax2.set_title(r'$O_3$')
    ax3.set_title(r'$PM2.5')

    ax1.plot(no2_day.index, no2_day['min'],
            '--b', label="min", linewidth=1)
    ax1.plot(no2_day.index, no2_day['max'],
            '--r', label="max", linewidth=1)
    ax1.legend()

    ax2.plot(o3_day.index, o3_day['min'],
            '--b', label="min", linewidth=1)
    ax2.plot(o3_day.index, o3_day['max'],
            '--r', label="max", linewidth=1)
    ax2.legend()

    ax3.plot(pm25_day.index, pm25_day['min'],
            '--b', label="min", linewidth=1)
    ax3.plot(pm25_day.index, pm25_day['max'],
            '--r', label="max", linewidth=1)
    ax3.legend()
    fig.savefig("img/daily_minmax.png")


def hourly_mean():
    fig, ax = plt.subplots()
    ax.set_xlabel("Hour")
    ax.set_ylabel("[µg/m³]")
    ax.plot(no2_hour, '-r', label=r'$NO_2$', linewidth=1)
    ax.plot(o3_hour, '-g', label=r'$O_3$', linewidth=1)
    ax.plot(pm25_hour, '-m',  label=r'$PM2.5$', linewidth=1)
    ax.legend()
    fig.savefig("img/hourly_mean.png")


def daily_mean():
    fig, ax = plt.subplots()
    ax.set_xlabel("Day")
    ax.set_ylabel("[µg/m³]")
    fig.set_figwidth(15)
    ax.plot(no2_day.index, no2_day['daily'],
            '-r', label=r'$NO_2$', linewidth=1)
    ax.plot(o3_day.index, o3_day['daily'], '-g', label=r'$O_3$', linewidth=1)
    ax.plot(pm25_day.index, pm25_day['daily'],
            '-m',  label=r'$PM2.5$', linewidth=1)
    ax.legend()
    fig.savefig("img/daily_mean.png")


def daily_mean_std():
    fig, (ax1, ax2) = plt.subplots(1, 2, sharex='col', layout='constrained')
    fig.supxlabel("Day")
    fig.supylabel("[µg/m³]")

    ax1.set_title(r'$NO_2$')
    ax2.set_title(r'$O_3$')

    fig.set_figwidth(20)
    ax1.errorbar(no2_day.index, no2_day['daily'], yerr=no2_day['std'],
                 mfc='blue', fmt='o', label=r'$NO_2$', capsize=3)
    ax2.errorbar(o3_day.index, o3_day['daily'], yerr=o3_day['std'],
                 mfc='blue', fmt='o', label=r'$O_3$', capsize=3)

    fig.savefig("img/daily_mean_std.png")


hourly_mean()
daily_mean()
daily_mean_std()
daily_minmax()
