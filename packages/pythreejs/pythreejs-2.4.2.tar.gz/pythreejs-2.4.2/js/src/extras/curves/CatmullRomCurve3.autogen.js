//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../../_base/serializers');

var ThreeModel = require('../../_base/Three.js').ThreeModel;


class CatmullRomCurve3Model extends ThreeModel {

    defaults() {
        return _.extend(ThreeModel.prototype.defaults.call(this), {


        });
    }

    constructThreeObject() {

        var result = new THREE.CatmullRomCurve3();
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        ThreeModel.prototype.createPropertiesArrays.call(this);




    }
}

CatmullRomCurve3Model.model_name = 'CatmullRomCurve3Model';
CatmullRomCurve3Model.serializers = {
    ...ThreeModel.serializers,
};

module.exports = {
    CatmullRomCurve3Model: CatmullRomCurve3Model,
};
