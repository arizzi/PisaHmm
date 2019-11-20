
#ifndef BOOSTTOCS_H
#define BOOSTTOCS_H

#include <utility>
#include <TLorentzVector.h>
#include "Math/GenVector/PxPyPzE4D.h"
#include "Math/GenVector/PtEtaPhiM4D.h"
#include "Math/GenVector/LorentzVector.h"
#include "Math/GenVector/LorentzRotation.h"
#include <TVector3.h>
#include <TMath.h>
#include <math.h>
#include <utility>      
#include <string>       
#include <iostream>   
#include <vector>   


// std::pair <float,float> boost_to_CS(const ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<float>> mu_Plus,const ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<float>> mu_Minus,const int& mucharge = -1)
// std::vector<float> pippo(const ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<float>> mu_Plus,const ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<float>> mu_Minus,const int& mucharge = -1)
std::pair<float,float> boost_to_CS(const ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<float>> mu_Plus,const ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<float>> mu_Minus, const int& mucharge = -1)
{
//         using namespace std;

        TLorentzVector muplus  = TLorentzVector( mu_Plus.Px(),  mu_Plus.Py(),  mu_Plus.Pz(),  mu_Plus.E());
        TLorentzVector muminus = TLorentzVector( mu_Minus.Px(), mu_Minus.Py(), mu_Minus.Pz(), mu_Minus.E());

        
        TLorentzVector Wv= muplus+muminus;// this is the Z boson 4vector

        float multiplier=mucharge; //Wv.Eta()*mucharge;//same as W charge

        TVector3 b = Wv.BoostVector();
        muplus.Boost(-b);
        muminus.Boost(-b);

        TLorentzVector PF = TLorentzVector(0,0,-6500,6500); 
        TLorentzVector PW = TLorentzVector(0,0,6500,6500); 

        PF.Boost(-b);
        PW.Boost(-b);
        bool PFMinus= true;
        // choose what to call proton and what anti-proton
        if(Wv.Angle(PF.Vect())<Wv.Angle(PW.Vect()))
        {
                PW= -multiplier*PW;
                PF= multiplier*PF;
        }
        else
        {
                PF= -multiplier*PF;
                PW= multiplier*PW;
                PFMinus=false;
        }
        PF=PF*(1.0/PF.Vect().Mag());
        PW=PW*(1.0/PW.Vect().Mag());

        // Bisector is the new Z axis
        TLorentzVector PBiSec =PW+PF;
        TVector3 PhiSecZ =  PBiSec.Vect().Unit();

        TVector3 PhiSecY = (PhiSecZ.Cross(Wv.Vect().Unit())).Unit();

        TVector3 muminusVec = muminus.Vect();
        TRotation roataeMe;

        // build matrix for transformation into CS frame
        roataeMe.RotateAxes(PhiSecY.Cross(PhiSecZ),PhiSecY,PhiSecZ);
        roataeMe.Invert();
        // tranfor into CS alos the "debugging" vectors
        muminusVec.Transform(roataeMe);

        float theta_cs = muminusVec.Theta();
        float cos_theta_cs = TMath::Cos(theta_cs);
        float phi_cs = muminusVec.Phi();

//         std::cout <<  theta_cs << " \t " <<cos_theta_cs << " \t " << phi_cs << " \t " <<std::endl;
         std::pair <float,float> CS_pair (cos_theta_cs, phi_cs);
	return CS_pair;
//         std::vector<float> CS_pair (cos_theta_cs, phi_cs);
//         std::vector<float> CS_pair;
//         CS_pair.push_back(cos_theta_cs);
//         CS_pair.push_back(phi_cs);
//         return CS_pair;

//        if (returnPhi) return phi_cs;
  //      if (returnPhi) return cos_theta_cs;
        
}

#endif
