import { Component, OnInit } from '@angular/core';
import { User } from '../models/user';
import { Subscription } from 'rxjs';
import { GlobalService } from '../services/global.service';
import { Router } from '@angular/router';
import { MovieService } from '../services/movie.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
  providers: [MovieService]
})
export class HomeComponent implements OnInit {

  account: User = new User();
  userSub: Subscription;

  constructor(private global: GlobalService, private router: Router, private movieService: MovieService) { }

  ngOnInit() {
    this.userSub = this.global.user.subscribe(
      me => this.account = me
    );
    if (localStorage.getItem('token') && localStorage.getItem('account')){
      this.global.me = JSON.parse(localStorage.getItem('account'));
      this.getMovies();
    }else{
      this.router.navigate(['/login'])
    }
  }
  getMovies(){
      this.movieService.getMovies().subscribe(
      movies => {
        console.log('movies',movies);

      },
      error => {
        console.log('error',error);
      }
    );
  }
  private logoutClicked(){
    this.global.me = new User();
    localStorage.removeItem('token');
    localStorage.removeItem('account');
    this.router.navigate(['/login']);
  }
}
