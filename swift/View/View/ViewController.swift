//
//  ViewController.swift
//  View
//
//  Created by patrick zierahn on 12.06.15.
//  Copyright (c) 2015 patrick zierahn. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var Button1: UIButton!
    @IBOutlet weak var Button2: UIButton!

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    @IBAction func Button1Pres(sender: AnyObject) {
 
        let storyBoard : UIStoryboard = UIStoryboard(name: "Main", bundle:nil)
        
        let nextViewController = storyBoard.instantiateViewControllerWithIdentifier("View2") as! ViewController2
        self.presentViewController(nextViewController, animated:true, completion:nil)
        
        println("Bla")
    }

}

