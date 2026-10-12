##  Definition

An ** Operating System ( OS)** is system  software that acts as  an **intermedi ary between computer  hardware and the user  ( or application  programs)**. It  manages hardware resources ( CPU, memory,  storage, I/O  devices) and provides  a  stable ,  consistent interface  for applications to run  without needing to know  hardware specifics .

**Core Respons ibilities:**
-  **Process Management:**  Scheduling, creation , termination, synchronization .
- **Memory  Management:** Allocation , deallocation , virtual memory,  protection .
- **File  System Management:** Organization , storage, retrieval , access  control.
- ** Device Management:** Driver  handling , I/O scheduling , buffering.
-  **Security & Protection :** Authentication , authorization, isolation .
- **User  Interface:** CLI  (Shell ), GUI,  System C alls ( API).

---

##  Types of Operating Systems 

|  Type  | Description  | Key  Characteristics | Typical Use  Cases /  Examples |
| : --- | :---  | :--- |  :--- |
|  **Batch OS ** | Jobs  grouped  in  batches; no  direct  user interaction. Operator  sorts  jobs with  similar needs . | High throughput ;  no  inter activity; difficult  to debug;  CPU  often  idle during  I/O. |  Historical mainframes ( IBM  OS /360 ), payroll,  billing systems. |
 | **Time-Sh aring /  Multitasking  OS** | CPU  time  sliced  among  multiple users/ processes simultaneously.  | Interactive;  quick  response time ; fair CPU  allocation; complex scheduling . | **Un ix, Linux,  Windows,  macOS**  (modern  general-purpose OSs ). |
| ** Real-Time OS ( RTOS)** |  Guarantees processing  within strict time  constraints (dead lines). Determ inism  >  Through put. | ** Hard RT OS :** Missing  deadline  = catastrophe (flight  control). <br>** Soft RTOS:**  Missing deadline = degraded  Qo S (stream ing). | V xWorks, Q NX, Free RTOS, AUT OSAR ( Aut omotive, Robot ics, Aerospace,  Medical). |
|  **Distributed OS ** | Manages  a group of independent  computers ( nodes) making  them appear as a  single coherent system.  | Resource  sharing; transparency ( location, migration );  high  availability ; complex  conc urrency control . | LOCUS , Amoeba , Plan  9;  modern  clusters (K ubernetes manages  containers , but kernel  is per -node). |
|  **Network OS ( NOS)** | Runs  on a server;  manages network resources,  users , security , data. Clients  request  services. | Central ized management; file /print sharing;  user authentication; server -cent ric. | ** Windows Server, Linux  (as  server ), Novell Net Ware ( legacy). ** |
| ** Embedded OS**  | Tail ored for specific hardware  with limited resources ( RAM/ ROM/CPU);  often  real -time capabilities . | Small footprint ; stripped -down  kernel; high reliability ; often mon olithic or  microkernel. |  FreeRTOS,  Zephyr, Embed ded Linux, Android  (mobile ), RT - Thread (IoT , Wearables,  Auto ). |
| ** Mobile OS** |  Optimized for touch ,  battery life , connectivity ,  sandboxing, ARM  architecture. | App  sandboxing; power  management; tele phony stack ; sensor integration.  | **Android ( Linux kernel ), iOS ( XNU kernel). ** |
| ** Multiprocessor  / Parallel OS**  | Designed for  systems with multiple CP Us sharing  memory ( SMP) or  interconnects ( NUMA). |  Load balancing;  cache  coherence ; thread synchronization;  scal ability. | Modern  Linux/ Windows/m acOS kernels ( all support  SMP/N UMA n atively). |
|  **Cluster OS ** | Lo osely coupled computers  working together for  High  Performance  Computing (HPC ) or High  Availability (HA).  | Message  passing ( MPI); single  system  image (SSI ) optional; fail over support . | Rocks  Cluster , OSC AR, Red  Hat Cluster  Suite  (Be owulf clusters ,  Supercomputers ). |

 ---

## Quick Classification  Che ats heet (Exam  Focus )

| Classification  Basis  | Categories  |
| :---  | :--- |
 | **User Interface ** | CLI  (D OS, Linux Server ), GUI (Windows , macOS,  Ubuntu Desktop), Touch  (Android , iOS).  |
| **Number  of Users** |  Single- User (MS-D OS, early Windows ), Multi-User  (Linux , Unix, Windows  Server). |
|  **Number of Tasks ** | Single-T asking (MS -DOS), Multi -Tasking ( All  modern OSs).  |
| **Processing  Method ** | Batch,  Interactive  (Time-Sh aring), Real-Time . |
| ** Architecture** |  Monolithic (Linux , traditional  Unix), Microkernel  (Minix,  QNX,  Harmony OS ), Hybrid (Windows  NT, macOS  XNU), Ex okernel (MIT  research ). |

---

##  Key Dist inction : Network  OS vs. Dist ributed OS
|  Feature | Network  OS |  Distributed OS |
| :--- |  :--- | : --- |
| ** Aw areness** | Users  ** know** they are  using remote  resources  (ex plicit login /m ount). | Users  **unaware**  of resource location;  transparency is  mandatory . |
| ** Autonomy** |  Nodes have  ** own local  OS**; cooperate  via protocols . | N odes run **part  of a  global OS**; kernels  cooperate  tightly . |
| ** Example** | Mapping  a network  drive in  Windows (` \\server \share`). |  Process migr ates automatically from  Node A to Node  B for load balancing . |

---

##  Summary for Dipl oma Ex ams
1.   **Define  OS:**  Resource Manager  + Extended  Machine.
 2.  **List Types :** Batch, Time -Sharing, Real -Time ( Hard/Soft),  Distributed, Network , Embedded,  Mobile.
3.   **Compare:**  RTOS vs.  GPOS (General  Purpose OS)  — Determ inism vs.  Fairness.
4 .  **Arch itecture:** Mon olithic vs. Micro kernel (know  examples : Linux vs . QNX /Minix). 
        