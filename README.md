<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/kea-roy/GraphAlgoVisualizer">
    <img src="https://github.com/kea-roy/GraphAlgoVisualizer/blob/main/images/logo.png" alt="Logo" width="80" height="80">
  </a>

<!-- PROJECT TITLE AND DESCRIPTION -->
<h3 align="center">Graph Algorithm Visualizer</h3>

  <p align="center">
    A Python application to visualize graph algorithms including:
    <br />
    ⁃ Depth First Search ⁃
    <br />
    ⁃ Breadth First Search ⁃
    <br />
    ⁃ Dijkstra's Shortest Path Algorithm ⁃
    <br />
    ⁃ Prim's Minimum Spanning Tree Algorithm ⁃
    <br />
    ⁃ Kruskal's Minimum Spanning Tree Algorithm ⁃
    <br />
    ⁃ Ford Fulkerson Maximum Flow Algorithm ⁃
    <br />
    <!--<a href="https://github.com/kea-roy/GraphAlgoVisualizer"><strong>Explore the docs »</strong></a>-->
    <br />
    <a href="https://github.com/kea-roy/GraphAlgoVisualizer/tree/main/src">View Code</a>
    ·
    <a href="https://github.com/kea-roy/GraphAlgoVisualizer/issues">Report Bug</a>
    ·
    <a href="https://github.com/kea-roy/GraphAlgoVisualizer/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Main Screen Shot][product-screenshot]

Over Fall 2023 winter break, I decided to spend some time refreshing my knowledge of several graph algorithms and to learn more about python networkx and tkinter visualization.

This project includes a simple user interface that guides the user through the input process step by step. The application supports a combination of file input and individual edge input with thorough checks to ensure the inputted graph meets the requirements for the algorithm selected.

The graph's node colors and edge colors change to show step by step iterations of the selected algorithm.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

<!--* [![Next][Next.js]][Next-url]-->
<!--* [![React][React.js]][React-url]-->
<!--* [![Vue][Vue.js]][Vue-url]-->
<!--* [![Angular][Angular.io]][Angular-url]-->
<!--* [![Svelte][Svelte.dev]][Svelte-url]-->
<!--* [![Laravel][Laravel.com]][Laravel-url]-->
<!--* [![Bootstrap][Bootstrap.com]][Bootstrap-url]-->
<!--* [![JQuery][JQuery.com]][JQuery-url]-->
<!--* [![Python][Python]][Python-url]-->
[![Python][Python]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, follow the instructions below:

### Prerequisites

This project requires the following dependencies to run:
* **matplotlib**
  ```sh
  pip install matplotlib
  ```
* **networkx**
  ```sh
  pip install networkx
  ```
* **tkinter**
  ```sh
  pip install tkinter
  ```
* **graphviz**

    See installation instructions at https://graphviz.gitlab.io/download/
* **pygraphviz**
 
    Note: graphviz must be installed first
  ```sh
  pip install pygraphviz
  ```
* **tktooltip**
  ```sh
  pip install tkinter-tooltip
  ```

### Installation

1. Ensure all prerequisites are installed correctly
2. Clone the repo
   ```sh
   git clone https://github.com/kea-roy/GraphAlgoVisualizer.git
   ```
3. Run ```__init__.py```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Demos

See below for several examples of the graph algorithm visualizer iterating through the different algorithms.

### Depth First Search
A depth first search starting at node A.

![Depth First Search GIF](https://github.com/kea-roy/GraphAlgoVisualizer/blob/main/images/dfs.gif)

### Breadth First Search
A breadth first search starting at node A.

![Breadth First Search GIF](https://github.com/kea-roy/GraphAlgoVisualizer/blob/main/images/bfs.gif)

### Dijkstra's
Dijkstra's algorithm for finding the shortest paths to all nodes from node A.

![Dijkstra GIF](https://github.com/kea-roy/GraphAlgoVisualizer/blob/main/images/dijkstras.gif)


### Prim's
Prim's algorithm for finding the minimum spanning tree of the connected graph

![Prims GIF](https://github.com/kea-roy/GraphAlgoVisualizer/blob/main/images/prims.gif)

### Kruskal's
Kruskal's algorithm for finding the minimum spanning tree of the connected graph

![Kruskals GIF](https://github.com/kea-roy/GraphAlgoVisualizer/blob/main/images/kruskals.gif)

### Ford-Fulkerson
Ford-Fulkerson algorithm to find the maximum flow from source node A to sink node H

![Ford-Fulkerson GIF](https://github.com/kea-roy/GraphAlgoVisualizer/blob/main/images/fordfulkerson.gif)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add Feature: Import Graph via File 
- [x] Add Feature: Import Graph via Edge
- [x] Add Features: Algorithm Support
    - [x] DFS
    - [x] BFS
    - [x] Dijkstra's
    - [x] Prim's
    - [x] Kruskal's
    - [x] Ford-Fulkerson
- [x] Add Feature: Previous and Next Iteration Button
- [x] Add Feature: ToolTip for Edge Input Format

See the [open issues](https://github.com/kea-roy/GraphAlgoVisualizer/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Kea-Roy Ong - ko353@cornell.edu

Project Link: [https://github.com/kea-roy/GraphAlgoVisualizer](https://github.com/kea-roy/GraphAlgoVisualizer)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

I would like to acknowledge the following resources that were used in the process of completing this project

* [NetworkX Official Documentation Site](https://networkx.org/documentation/stable/reference/index.html)
* [NeuralNine: NetworkX Crash Course - Graph Theory in Python
](https://www.youtube.com/watch?v=VetBkjcm9Go)
* [Stack Overflow: NetworkX Tkinter Ford-Fulkerson Question](https://stackoverflow.com/questions/55553845/display-networkx-graph-inside-the-tkinter-window)
* [othneildrew's README Template](https://github.com/othneildrew/Best-README-Template)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/kea-roy/GraphAlgoVisualizer.svg?style=for-the-badge
[contributors-url]: https://github.com/kea-roy/GraphAlgoVisualizer/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/kea-roy/GraphAlgoVisualizer.svg?style=for-the-badge
[forks-url]: https://github.com/kea-roy/GraphAlgoVisualizer/network/members
[stars-shield]: https://img.shields.io/github/stars/kea-roy/GraphAlgoVisualizer.svg?style=for-the-badge
[stars-url]: https://github.com/kea-roy/GraphAlgoVisualizer/stargazers
[issues-shield]: https://img.shields.io/github/issues/kea-roy/GraphAlgoVisualizer.svg?style=for-the-badge
[issues-url]: https://github.com/kea-roy/GraphAlgoVisualizer/issues
[license-shield]: https://img.shields.io/github/license/kea-roy/GraphAlgoVisualizer.svg?style=for-the-badge
[license-url]: https://github.com/kea-roy/GraphAlgoVisualizer/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/kea-roy
[product-screenshot]: images/mainscreenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
