#!/usr/bin/env python3

import karabo_data

run_path = "/gpfs/exfel/exp/SPB/201701/p002012/raw/r0244"

run = karabo_data.RunDirectory(run_path)

run = run.select("*/DET/*", "*")

run = run.select_trains(karabo_data.by_id[[76961506, 76961507, 76961508, 76961509]])

run.write("data_subset.h5")
