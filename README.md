<p>The idea was derived from <b>Stable Marriage Problem.</b></p>
<p>Due to wikipedia:</p>
<p><i>
The stable marriage problem has been stated as follows:</br>
Given n men and n women, where each person has ranked all members of the opposite sex in order of preference, marry the men and women together such that there are no two people of opposite sex who would both rather have each other than their current partners. When there are no such pairs of people, the set of marriages is deemed stable.
</i></p>

<p>Script explanation:</p>
<ul>
  <li>6 Project Coordinators</li>
  <li>6 Suppliers</li>
  <li>Each single coordinator and supplier is called 'party' in the script</li>
  <li>Number of parties can be set in the script</li>
  <li>Constraints: number of coordinators = number of suppliers</li>
  <li>Each party has its own 6 items list of preferences</li>
  <li>
    Project Coordinators chooses preffered Suppliers in the descending order of preference starting from the most preffred one and vice versa
  </li>
  <li>Script uses random library to shuffle prefrerences for each party</li>
  <li>Script matches coordinator-suppliers pairs according to their preferences list</li>
  <li>
    Script continues matching and breaking matches till we have all the parties matched up and, what is most important, no one from the pairs has better preffered option - it's called a stable match
  </li>
</ul>

<p>Outcome:</p>
<img src="images/outcome.JPG", height="480", width="280">
