<script type="text/javascript">
function setFourthWednesdayOfQuarter(dt) {
    // Calculate the first month of the quarter containing dt.
    var tmp = dt.getMonth();
    tmp = tmp - tmp % 3;
    dt.setMonth(tmp);
    // The earliest possible 4th Wednesday of a month is the 22nd.
    dt.setDate(22);
    /*
      We need to determine when the first Wednesday is from the 22nd.
      In JavaScript dates, Sunday is 0, so Wednesday is 3.  For
      comprehension, here is a table of how many days need to be added
      to the 22nd to get to a Wednesday depending on what day of the
      week the the 22nd is on and the math for calculating it:

       Day of Week of    Days to add to
       the 22nd (DOW22)  get to a Wed.   10 - DOW22   (10 - DOW22) % 7
       ----------------  --------------  -----------  ----------------
            Sunday=0           3         10 - 0 = 10  (10 - 0) % 7 = 3
            Monday=1           2         10 - 1 = 9   (10 - 1) % 7 = 2
           Tuesday=2           1         10 - 2 = 8   (10 - 2) % 7 = 1
         Wednesday=3           0         10 - 3 = 7   (10 - 3) % 7 = 0
          Thursday=4           6         10 - 4 = 6   (10 - 4) % 7 = 6
            Friday=5           5         10 - 5 = 5   (10 - 5) % 7 = 5
          Saturday=6           4         10 - 6 = 4   (10 - 6) % 7 = 4

      Note that the results of the math in the last column match the
      desired results from the second column.
    */
    dt.setDate(dt.getDate() + (10 - dt.getDay()) % 7);
}

function setNextQuarter(dt) {
    dt.setMonth(dt.getMonth() + 3);
}

function setMeetN(dt, n) {
    document.getElementById('meet' + n).innerText =
	dt.toLocaleDateString([], {year: 'numeric',
				   month: 'long',
				   day: 'numeric'});
}

var now = new Date();
var dt = new Date(now);
var i = 1;
do {
    setFourthWednesdayOfQuarter(dt);
    if (now <= dt) {
	setMeetN(dt, i);
	i += 1;
    }
    setNextQuarter(dt);
} while (i < 5);
</script>
