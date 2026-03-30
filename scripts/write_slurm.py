#!/usr/bin/env python3
# write_slurm.py

# User variables
job_name = "blast_watermelon"
hours = "01:00:00"
queue = "cloud72"
email = "your_email@example.com"

# Print SLURM script
print("#!/bin/bash\n")
print(f"#SBATCH --job-name={job_name}")
print(f"#SBATCH --partition={queue}")
print("#SBATCH --nodes=1")
print("#SBATCH --qos=cloud")
print("#SBATCH --ntasks=1")
print("#SBATCH --cpus-per-task=32")   # Number of threads
print(f"#SBATCH --time={hours}")
print("#SBATCH --output=%x.%j.out")
print("#SBATCH --error=%x.%j.err")
print(f"#SBATCH --mail-type=ALL")
print(f"#SBATCH --mail-user={email}\n")

# Environment variables (print them to SLURM script)
print("export OMP_NUM_THREADS=32\n")

# Modules
print("module purge")
print("module load blast\n")

# Change to submission directory
print("cd $SLURM_SUBMIT_DIR\n")

# BLAST commands
print("makeblastdb -in watermelon.fsa -dbtype nucl")
print("blastn -query watermelon.fsa -subject watermelon.fsa > wat.vs.wat.blastn")




