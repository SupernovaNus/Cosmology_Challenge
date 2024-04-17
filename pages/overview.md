# Overview 
***

## Problem summary
***
Each weak lensing map is constructed from three simulation boxes covering different redshift ranges, with different box sizes and resolutions. The priors over which cosmological parameters are samples are:

$0.06 < \Omega_m < 0.65$ and $0.662 < S_8 < 0.966$

Fix cosmological parameters: $h=0.7$, $\Omega_b=0.046$, $n_s=0.97$ (to the same as the HSC modck simulations).

### Largest box covering $z>1$ of size 1536 Mpc/h

This box uses the FastPM quasi N-body code with $1536^3$ particles and 0.5 Mpc/h force resolution and 15 times steps.

### Medium box covering $0.42<z<1$ of size 704 Mpc/h

This box uses the FastPM code with $2816^3$ particles and 0.125 Mpc/h force resolution and 60 time steps.

### Smallest box covering $z<0.42$ of size 320 Mpc/h

This simulation uses MP-Gadget and has $960^3$ particles with 0.03 Mpc/h force resolution with adaptive time steps.



There are 101 cosmologies in total. Each particle has an associated position and velocity, and is captured at 19 timessteps so is described by 6x19=114 Float32 numbers. The total number of particles in each box differs, and so the total size in each box is:

- 1536 Mpc/h box:  $3 \times 32~{\rm Bits} \times (1536^3~{\rm particles}) * (101~{\rm cosmologies}) * (16~{\rm Snapshots}) = 83.4~{\rm TB}$
- 704 Mpc/h box: $3 \times 32~{\rm Bits} \times (2816^3~{\rm particles}) * (101~{\rm cosmologies}) * (19~{\rm Snapshots}) = 1.2~{\rm TB}$
- 320 Mpc/h box: $3 \times 32~{\rm Bits} \times (960^3~{\rm particles}) * (101~{\rm cosmologies}) = 0.1~{\rm TB}$


## How to join this challenge?
***
- Go to the "Starting Kit" tab
- Download the "Dummy sample submission" or "sample submission"
- Go to the "My Submissions" tab
- Submit the downloaded file

For more instructions feel free to checkout these [Tutorial Slides](https://fair-universe.lbl.gov/tutorials/HiggsML_Uncertainty_Challenge-Codabench_Tutorial.pdf) 


## Submissions
***
This competition allows code submissions. Participants can submit either of the following:
- code submission without any trained model
- code submission with pre-trained model

## Credits
***
#### Lawrence Berkeley National Laboratory 
- Benjamin Nachman
- Ben Thorne
- Chris Harris
- Sascha Diefenbacher
- Steven Farrell
- Wahid Bhimji

#### University of Washington
- Elham E Khoda
- Shih-Chieh Hsu

#### ChaLearn
- Isabelle Guyon
- Ihsan Ullah

#### Université Paris-Saclay
- David Rousseau
- Ragansu Chakkappai

#### UC Irvine
- Aishik Ghosh


## Contact
***
Visit our website: https://fair-universe.lbl.gov/

Email: fair-universe@lbl.gov

Updates will be announced through fair-universe-announcements google group. [Click to join Google Group](https://groups.google.com/u/0/a/lbl.gov/g/Fair-Universe-Announcements/)